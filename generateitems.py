from openomp import app, db
from openomp.models import Item, User
import os

def run(count):
    db.drop_all()
    db.create_all()

    user = User(username='123451234512345', hashed_password='123456789012345678901234567890123456789012345678901234567890')
    db.session.add(user)
    db.session.commit()

    for i in range(1, count+1):
        description = 'This is the description of this item. The goal of the description is to give the visitor an overview of the functionality of the item in question.'
        thumbnail_img = None
        with open(f"{os.path.join(app.root_path,'static','placeholder_icon.png')}", 'rb') as file:
                data = file.read()
                thumbnail_img = data
        item = Item(title='Item', description=description, thumbnail_img=thumbnail_img, user_id=user.id)
        db.session.add(item)
        db.session.commit()
        print(f'Finished {i}/{count}')

    user = User(username='098765098765098765', hashed_password='123456789012345678901234567890123456789012345678901234567890')
    db.session.add(user)
    db.session.commit()

    description = 'This is the description of this item. The goal of the description is to give the visitor an overview of the functionality of the item in question.'
    thumbnail_img = None
    with open(f"{os.path.join(app.root_path,'static','placeholder_icon.png')}", 'rb') as file:
            data = file.read()
            thumbnail_img = data
    item = Item(title='Item', description=description, thumbnail_img=thumbnail_img, user_id=user.id)
    db.session.add(item)
    db.session.commit()

if __name__ == '__main__':
    run(500)