from openomp import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    hashed_password = db.Column(db.String(60), nullable=False)
    items = db.relationship('Item', backref='user', lazy=True)
    #messages = db.relationship('Message', backref='user', lazy=True)

    def __repr__(self):
        return f'User("{self.username}","{self.password}")'

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, nullable= False, default=datetime.utcnow)
    thumbnail_img = db.Column(db.LargeBinary, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item("{self.title}","{self.description}","{self.date_created}")'
'''
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    date_sent = db.Column(db.DateTime, nullable= False, default=datetime.utcnow)
    text = db.Column(db.String(500), nullable=False)
    '''
