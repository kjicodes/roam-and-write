from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField, PasswordField, EmailField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, Length, Email, NumberRange, URL, Optional


class RegisterForm(FlaskForm):
    first_name = StringField('First Name*', validators=[DataRequired()])
    last_name = StringField('Last Name*', validators=[DataRequired()])
    email = EmailField('Email*', validators=[Email(), DataRequired()])
    password = PasswordField('Password*', validators=[DataRequired()])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email*', validators=[DataRequired()])
    password = StringField('Password*', validators=[DataRequired()])
    submit = SubmitField('Login')


class CreatePostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    location = StringField('Destination ✈️ (e.g. City, Prov/State, Country)', validators=[DataRequired()])
    num_times_visited = IntegerField('How many times have you visited?', validators=[NumberRange(min=1, message="Value must be above 0."), DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired()])
    visit_again = BooleanField('Would you visit again?')
    rating = SelectField('How many stars?', choices=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], validators=[DataRequired()])
    img_url = StringField('Image URL', validators=[Optional(), URL()])
    submit = SubmitField('Submit')
