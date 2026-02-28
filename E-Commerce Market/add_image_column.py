from market import app, db
from sqlalchemy import inspect, text

with app.app_context():
    inspector = inspect(db.engine)
    print('tables:', inspector.get_table_names())
    if 'user' in inspector.get_table_names():
        cols = [c['name'] for c in inspector.get_columns('user')]
        print('user columns before:', cols)
        if 'image' not in cols:
            with db.engine.connect() as conn:
                conn.execute(text('ALTER TABLE user ADD COLUMN image VARCHAR(200) NOT NULL DEFAULT ""'))
            print('user image column added.')
        else:
            print('user image column already exists.')
    if 'item' in inspector.get_table_names():
        cols_item = [c['name'] for c in inspector.get_columns('item')]
        print('item columns before:', cols_item)
        if 'image' not in cols_item:
            with db.engine.connect() as conn:
                conn.execute(text('ALTER TABLE item ADD COLUMN image VARCHAR(200)'))
            print('item image column added.')
        else:
            print('item image column already exists.')