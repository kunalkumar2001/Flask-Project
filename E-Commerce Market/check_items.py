from market import app, db
from market.models import Item

with app.app_context():
    items = Item.query.all()
    for item in items:
        owner_name = "Unowned" if item.owner is None else f"Owned (user_id={item.owner})"
        print(f"{item.name}: {owner_name}")
