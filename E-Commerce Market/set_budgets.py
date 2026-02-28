from market import app, db
from market.models import User

with app.app_context():
    users = User.query.all()
    for u in users:
        print(f"Setting {u.username} budget from {u.budget} to 10000")
        u.budget = 10000
    db.session.commit()
    print("Budgets updated.")
