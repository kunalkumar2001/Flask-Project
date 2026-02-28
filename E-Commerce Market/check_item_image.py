from market import app, db
from market.models import Item

with app.app_context():
    item = Item.query.filter_by(name='Laptop').first()
    print('image field:', item.image)
    print('full path should be:', app.static_url_path + '/' + item.image)
