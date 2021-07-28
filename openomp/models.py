from openomp import db
from datetime import datetime
from flask_login import UserMixin


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, nullable= False, default=datetime.utcnow)
    thumbnail_img = db.Column(db.LargeBinary, nullable=False)

    def __repr__(self):
        return f'Item("{self.title}","{self.description}","{self.date_created}")'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    #messages = db.relationship('Message', backref='user', lazy=True)

    def __repr__(self):
        return f'User("{self.username}","{self.password}")'
'''
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_sent = db.Column(db.DateTime, nullable= False, default=datetime.utcnow)
    text = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'Message("{self.sender_id}","{self.receiver_id}","{self.date_sent}","{self.text}")'
'''