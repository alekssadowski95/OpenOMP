from openomp import app, db
from openomp.models import Item, User
import random
import os

def run():
    db.drop_all()
    db.create_all()

    TITLE = 'Hand-crafted cup'
    SHORT_DESCRIPTION = 'This cup has been crafted by a local family'
    LONG_DESCRIPTION = 'This cup is the right gift for any person drinking coffee or tea. It has been crafted by a small company that uses local resources. Every single cup has gone through many hands during its production process. Thanks to that, only perfect cups get shipped out.'

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

    user1 = User(username='RonSchmitz', hashed_password='123456789012345678901234567890123456789012345678901234567890')
    db.session.add(user1)
    db.session.commit()

    user2 = User(username='AlinaSchwartz', hashed_password='123456789012345678901234567890123456789012345678901234567890')
    db.session.add(user2)
    db.session.commit()

    user3 = User(username='JessicaGeller', hashed_password='123456789012345678901234567890123456789012345678901234567890')
    db.session.add(user3)
    db.session.commit()

    for i in range(len(images)):
        thumbnail_img = None
        with open(f"{os.path.join(app.root_path,'static','sample', 'images', images[i])}", 'rb') as file:
                data = file.read()
                thumbnail_img = data
        item = Item(title=TITLE, short_description=SHORT_DESCRIPTION, long_description=LONG_DESCRIPTION, thumbnail_img=thumbnail_img, user_id=random.randint(1,3))
        db.session.add(item)
        db.session.commit()


if __name__ == '__main__':
    run()