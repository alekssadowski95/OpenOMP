from openomp import app, db
from flask import render_template, redirect, url_for, request
from .forms import AddItemForm
from .models import Item
import os
from sqlalchemy import desc
import base64

def get_thumbnail(configurator):
    thumbnail = base64.b64encode(configurator.thumbnail_img).decode('ascii')
    return thumbnail

@app.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    items = Item.query.order_by(desc(Item.id)).paginate(page=page, per_page=48)
    return render_template('home.html', items=items, get_thumbnail=get_thumbnail)

@app.route('/add-item', methods=['GET', 'POST'])
def add_item():
    add_item_form = AddItemForm()
    if add_item_form.validate_on_submit():
        print('Added item')
        thumbnail_img = None
        if add_item_form.item_image.data:
            thumbnail_img = request.files[add_item_form.item_image.name].read()
        else:
            with open(f"{os.path.join(app.root_path,'static','placeholder_icon.png')}", 'rb') as file:
                data = file.read()
                thumbnail_img = data
        item = Item(title=add_item_form.title.data, description=add_item_form.description.data, thumbnail_img=thumbnail_img)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('additem.html', title='Add your item', form=add_item_form) 
