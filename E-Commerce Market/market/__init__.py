from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '8beef40d712af75ab4e3134c'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'

# ensure database schema is current (add missing columns)
from sqlalchemy import inspect, text
with app.app_context():
    inspector = inspect(db.engine)
    # create tables if necessary
    if 'user' not in inspector.get_table_names() or 'item' not in inspector.get_table_names():
        db.create_all()
    else:
        # ensure user.image
        cols = [c['name'] for c in inspector.get_columns('user')]
        if 'image' not in cols:
            with db.engine.connect() as conn:
                conn.execute(text('ALTER TABLE user ADD COLUMN image VARCHAR(200) NOT NULL DEFAULT ""'))
        # ensure item.image
        cols_item = [c['name'] for c in inspector.get_columns('item')]
        if 'image' not in cols_item:
            with db.engine.connect() as conn:
                conn.execute(text('ALTER TABLE item ADD COLUMN image VARCHAR(200)'))


from market import models
from market import routes

@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))