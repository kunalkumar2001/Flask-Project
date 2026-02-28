from market import app, db
from market.models import Item

with app.app_context():
    iphone = Item.query.filter_by(name="iPhone").first()
    if iphone:
        iphone.owner = None
        db.session.commit()
        print("iPhone is now unowned and will appear in market grid")
    else:
        print("iPhone not found")
