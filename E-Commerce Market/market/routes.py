from market import app, db, bcrypt
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from flask_login import login_user, logout_user, login_required, current_user


# ================= HOME =================

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


# ================= MARKET =================

@app.route('/market', methods=['GET', 'POST'])
@login_required
def market_page():

    purchase_form = PurchaseItemForm()
    selling_form = SellItemForm()

    # HANDLE POST REQUEST (Purchase / Sell)
    if request.method == "POST":

        # ===== PURCHASE LOGIC =====

        purchased_item = request.form.get('purchased_item')

        if purchased_item:

            item_object = Item.query.filter_by(name=purchased_item).first()

            if item_object:

                if current_user.can_purchase(item_object):

                    item_object.buy(current_user)

                    flash(
                        f"✅ You purchased {item_object.name} for ${item_object.price}",
                        category='success'
                    )

                else:

                    flash(
                        f"❌ You don't have enough budget for {item_object.name}",
                        category='danger'
                    )


        # ===== SELL LOGIC =====

        sold_item = request.form.get('sold_item')

        if sold_item:

            item_object = Item.query.filter_by(name=sold_item).first()

            if item_object:

                if current_user.can_sell(item_object):

                    item_object.sell(current_user)

                    flash(
                        f"💰 You sold {item_object.name} back to market",
                        category='success'
                    )

                else:

                    flash(
                        f"❌ Cannot sell {item_object.name}",
                        category='danger'
                    )


        return redirect(url_for('market_page'))


    # ===== GET REQUEST =====

    items = Item.query.filter_by(owner=None).all()

    owned_items = Item.query.filter_by(owner=current_user.id).all()


    return render_template(
        'market.html',
        items=items,
        owned_items=owned_items,
        purchase_form=purchase_form,
        selling_form=selling_form
    )



# ================= REGISTER =================

@app.route('/register', methods=['GET', 'POST'])
def register_page():

    form = RegisterForm()

    if form.validate_on_submit():

        hashed_password = bcrypt.generate_password_hash(
            form.password1.data
        ).decode('utf-8')

        user_to_create = User(
            username=form.username.data,
            email_address=form.email_address.data,
            password_hash=hashed_password
        )

        db.session.add(user_to_create)
        db.session.commit()

        login_user(user_to_create)

        flash(
            f"🎉 Account created successfully! Welcome {user_to_create.username}",
            category='success'
        )

        return redirect(url_for('market_page'))


    if form.errors:

        for err_msg in form.errors.values():

            flash(
                f"❌ Error creating user: {err_msg}",
                category='danger'
            )


    return render_template('register.html', form=form)



# ================= LOGIN =================

@app.route('/login', methods=['GET', 'POST'])
def login_page():

    form = LoginForm()

    if form.validate_on_submit():

        attempted_user = User.query.filter_by(
            username=form.username.data
        ).first()

        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data):

            login_user(attempted_user)

            flash(
                f"✅ Welcome back, {attempted_user.username}",
                category='success'
            )

            return redirect(url_for('market_page'))

        else:

            flash(
                "❌ Username or password incorrect",
                category='danger'
            )


    return render_template('login.html', form=form)



# ================= LOGOUT =================

@app.route('/logout')
@login_required
def logout_page():

    logout_user()

    flash(
        "👋 You have been logged out successfully",
        category='info'
    )

    return redirect(url_for('home_page'))