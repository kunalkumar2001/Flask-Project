from market import app, db
from market.models import Item

with app.app_context():
    items = Item.query.all()
    for i in items:
        print(i.name, i.price, getattr(i, 'image', None))
