from openomp import app, db, bcrypt
from .forms import AddItemForm, LoginForm, RegisterForm
from .models import Item, User

from flask import render_template, redirect, url_for, request
from flask_login import login_user
from sqlalchemy import desc

import os
import base64

def get_thumbnail(item):
    thumbnail = base64.b64encode(item.thumbnail_img).decode('ascii')
    return thumbnail

@app.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    items = Item.query.order_by(desc(Item.id)).paginate(page=page, per_page=48)
    return render_template('home.html', items=items, get_thumbnail=get_thumbnail)

@app.route('/item/<id>')
def item(id):
    current_item = Item.query.filter_by(id = id).first()
    return render_template('item.html', item=current_item, get_thumbnail=get_thumbnail)

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))             
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # create new user
        return redirect(url_for('home'))
    return render_template('register.html', form=form)
