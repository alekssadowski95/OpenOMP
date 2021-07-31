from flask.helpers import flash
from openomp import app, db, bcrypt
from .forms import AddItemForm, LoginForm, RegisterForm
from .models import Item, User

from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user, current_user
from sqlalchemy import desc

import os
import base64

def get_thumbnail(item):
    ''' Get thumbnail from data object and return in ascii
    '''
    thumbnail = base64.b64encode(item.thumbnail_img).decode('ascii')
    return thumbnail

@app.route('/')
def home():
    ''' Homepage
    '''
    page = request.args.get('page', 1, type=int)
    items = Item.query.order_by(desc(Item.id)).paginate(page=page, per_page=48)
    return render_template('home.html', items=items, get_thumbnail=get_thumbnail)

@app.route('/item/<id>')
def item(id):
    ''' Show an existing item.
    '''
    item = Item.query.filter_by(id = id).first()
    user = User.query.filter_by(id = item.user_id).first()
    if item:
        return render_template('item.html', item=item, get_thumbnail=get_thumbnail, user=user)
    return redirect(url_for('home'))

@app.route('/add-item', methods=['GET', 'POST'])
def add_item():
    ''' Add a new item.
    '''
    if current_user.is_authenticated:
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
            item = Item(title=add_item_form.title.data, description=add_item_form.description.data, thumbnail_img=thumbnail_img, user_id=current_user.id)
            db.session.add(item)
            db.session.commit()
            return redirect(url_for('home'))
        return render_template('additem.html', title='Add your item', form=add_item_form) 
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    ''' Login an existing user.
    '''
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.hashed_password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))             
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    ''' Create a new user.
    '''
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, hashed_password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('You successfully registered your account.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/messages')
def messages():
    ''' Show the messages of the current user.
    '''
    if current_user.is_authenticated:
        return render_template('messages.html', title='Messages')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    ''' Logout the current user.
    '''
    if current_user.is_authenticated:
        logout_user()
        flash('You successfully logged out.', 'success')
        return redirect(url_for('home'))   
    return redirect(url_for('home'))

@app.route('/user/<id>')
def user(id):
    ''' Show user profile page
    '''
    user = User.query.filter_by(id = id).first()
    if user:
        return render_template('user.html', user=user)
    else:
        return redirect(url_for('home'))

@app.route('/credits')
def credits():
    return render_template('credits.html')
