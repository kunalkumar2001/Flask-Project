from market import app, db
from market.models import Item

# this script updates the image paths for specific items
mappings = {
    "Laptop": "images/laptop.png",
    "iPhone": "images/phone.png",
    "Keyboard": "images/keyboard.png",
}

with app.app_context():
    for name, path in mappings.items():
        item = Item.query.filter_by(name=name).first()
        if item:
            item.image = path
            print(f"Setting image for {name} -> {path}")
        else:
            print(f"Item '{name}' not found in database")
    db.session.commit()
    print("Done updating images.")
