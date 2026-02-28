from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from market.models import User

class RegisterForm(FlaskForm):
    username = StringField(
        label='Username',
        validators=[DataRequired(), Length(min=3, max=25)]
    )

    email_address = StringField(
        label='Email Address',
        validators=[DataRequired(), Email()]
    )

    password1 = PasswordField(
        label='Password',
        validators=[DataRequired(), Length(min=6)]
    )

    password2 = PasswordField(
        label='Confirm Password',
        validators=[DataRequired(), EqualTo('password1')]
    )

    submit = SubmitField(label='Create Account')


    def validate_username(self, username_to_check):
        user = User.query.filter_by(
            username=username_to_check.data
        ).first()

        if user:
            raise ValidationError(
                'Username already exists! Please try a different username.'
            )

    
    def validate_email_address(self, email_to_check):
        email = User.query.filter_by(
            email_address=email_to_check.data
        ).first()

        if email:
            raise ValidationError(
                'Email already registered!'
            )


class LoginForm(FlaskForm):
    username = StringField(
        label='Username',
        validators=[DataRequired()]
    )

    password = PasswordField(
        label='Password',
        validators=[DataRequired()]
    )

    submit = SubmitField(label='Sign In')
    
    
class PurchaseItemForm(FlaskForm):
    submit_purchase = SubmitField(label='Purchase Item')
    
    
class SellItemForm(FlaskForm):
    submit_sell = SubmitField(label='Sell Item')