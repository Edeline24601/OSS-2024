from wsgiref.validate import validator

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class TODOForm(FlaskForm):
    priority = IntegerField
    content = TextAreaField
    done = BooleanField

class UserSignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo('password_check', 'Password does not match')])
    password_check = PasswordField("Confirm Password", validators=[DataRequired()])

class UserLoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField("Password", validators=[DataRequired()])