from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,Email,InputRequired,EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
	firstname = StringField('Firstname', validators=[DataRequired()]) 
	lasttname = StringField('Lastname', validators=[DataRequired()]) 
	email = StringField('Email', validators=[DataRequired(),Email()])
	password = PasswordField('New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
	confirm  = PasswordField('Repeat Password')
	submit = SubmitField('Sign Up')
