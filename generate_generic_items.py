from openomp import app, db
from openomp.models import Item, User
import os

def run(count):
    db.drop_all()
    db.create_all()

    images = [
        'pexels-anna-nekrashevich-8533397.jpg',
        'pexels-anna-pou-8329247.jpg',
        'pexels-anna-pou-8329871.jpg',
        'pexels-archie-binamira-1187317.jpg',
        'pexels-beyza-efe-8340102.jpg',
        'pexels-dominika-roseclay-894608.jpg',
        'pexels-ena-marinkovic-4071737.jpg',
        'pexels-julia-filirovska-8257939.jpg',
        'pexels-julia-sakelli-905485.jpg',
        'pexels-lilartsy-1721090.jpg',
        'pexels-los-muertos-crew-8279911.jpg',
        'pexels-marina-m-8356299.jpg',
        'pexels-marina-m-8356386.jpg',
        'pexels-polina-tankilevitch-4109853.jpg',
        'pexels-rachel-claire-4577860.jpg',
        'pexels-skylar-kang-6207307.jpg',
        'pexels-solodsha-8105127.jpg',
        'pexels-wagamamaakko-8479555.jpg',
        'pexels-zen-chung-5749084.jpg',
        'pexels-дарья-сергунина-8306605.jpg'
    ]

    user = User(username='JamieLannister', hashed_password='123456789012345678901234567890123456789012345678901234567890')
    db.session.add(user)
    db.session.commit()

    for i in range(1, count+1):
        short_description = 'This is the short description'
        long_description = 'This is the description of this item. The goal of the description is to give the visitor an overview of the functionality of the item in question.'
        thumbnail_img = None
        with open(f"{os.path.join(app.root_path,'static','placeholder_icon.png')}", 'rb') as file:
                data = file.read()
                thumbnail_img = data
        item = Item(title='title', short_description=short_description, long_description=long_description, thumbnail_img=thumbnail_img, user_id=1)
        db.session.add(item)
        db.session.commit()
        print(f'Finished {i}/{count}')

    user = User(username='ElisabethSwan', hashed_password='123456789012345678901234567890123456789012345678901234567890')
    db.session.add(user)
    db.session.commit()

    short_description = 'This is the short description'
    long_description = 'This is the description of this item. The goal of the description is to give the visitor an overview of the functionality of the item in question.'
    thumbnail_img = None
    with open(f"{os.path.join(app.root_path,'static','placeholder_icon.png')}", 'rb') as file:
            data = file.read()
            thumbnail_img = data
    item = Item(title='title', short_description=short_description, long_description=long_description, thumbnail_img=thumbnail_img, user_id=2)
    db.session.add(item)
    db.session.commit()

if __name__ == '__main__':
    run(100)