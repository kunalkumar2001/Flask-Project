from market import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length = 30), nullable = False, unique = True)
    email_address = db.Column(db.String(length = 50),nullable = False, unique = True)
    password_hash = db.Column(db.String(length = 60), nullable = False)
    budget = db.Column(db.Integer(), nullable=False, default = 10000)
    items = db.relationship('Item', backref = 'owned_user',lazy=True)
    image = db.Column(db.String(length=200), nullable=False)
  
    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]} $'
        else:
            return f'{self.budget} $'
  
    @property
    def password(self):
        return self.password_hash
    
    @password.setter
    def password(self, plain_text_password):
        from market import bcrypt
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
        
    def check_password_correction(self, attempted_password):
        from market import bcrypt
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
    
    def can_purchase(self, item_obj):
        return self.budget >= item_obj.price

    def can_sell(self, item_obj):
        # user can sell if they own the item
        return item_obj.owner == self.id
    

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    image = db.Column(db.String(length=200), nullable=True)

    def __repr__(self):
        return f'Item {self.name}'
    
    
    def buy(self, user):
        user.budget -= self.price
        self.owner = user.id
        db.session.commit()


    def sell(self, user):
        user.budget += self.price
        self.owner = None
        db.session.commit()
        