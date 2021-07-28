from openomp import app, db
from openomp.models import Item
import os

def run(count):
    db.drop_all()
    db.create_all()
    for i in range(1, count+1):
        description = 'This is the description of this item. The goal of the description is to give the visitor an overview of the functionality of the item in question.'
        thumbnail_img = None
        with open(f"{os.path.join(app.root_path,'static','placeholder_icon.png')}", 'rb') as file:
                data = file.read()
                thumbnail_img = data
        item = Item(title='Item', description=description, thumbnail_img=thumbnail_img)
        db.session.add(item)
        db.session.commit()
        print(f'Finished {i}/{count}')

if __name__ == '__main__':
    run(500)