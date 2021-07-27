from openomp import db
from datetime import datetime


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, nullable= False, default=datetime.utcnow)
    thumbnail_img = db.Column(db.LargeBinary, nullable=False)