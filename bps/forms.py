from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,Email,InputRequired,EqualTo,Length
from wtforms.validators import DataRequired,Email,InputRequired,EqualTo
from wtforms.validators import DataRequired,Email,InputRequired,EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(),Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
	firstName = StringField('Firstname', validators = [DataRequired()]) 
	lastName = StringField('Lastname', validators = [DataRequired()]) 
	email = StringField('Email', validators = [DataRequired(),Email()])
	employId = StringField('Employ Id', validators = [DataRequired()])
	password = PasswordField('New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match'), Length(min=8, message = 'Password should contain minimum eight characters')])
	confirm  = PasswordField('Repeat Password', [InputRequired(),Length(min=8, message = 'Password should contain minimum eight characters')])
	submit = SubmitField('Create Account')

# this is a class to add a search box in the products info. page.
# main usage in : bps>main>working>productInfo
class SearchBarForm(FlaskForm):
	searchFor = StringField('Search', validators = [DataRequired()])
	submit = SubmitField('Search')

