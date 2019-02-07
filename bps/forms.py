from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,Email,InputRequired,EqualTo
#import keyboard as kb
import pymysql as db

host = "localhost"
user = "AKSHAY"
password = "23232213"
database = "pharmacy"
port = 3306

connection = db.connect(host,user,password,database,port)
cursor = connection.cursor()


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
	def UniqueId(form,field):
		if keyboard.KEY_DOWN :
			string = form.employId
			res = cursor.execute("SELECT 'FIRSTNAME' FROM Admin WHERE 'EMPLOY_ID'= {}",{string})
			if res > 0:
				raise ValidationError('An admin with this EMPLOY_ID already exists!!')

	firstName = StringField('Firstname', validators=[DataRequired()]) 
	lastName = StringField('Lastname', validators=[DataRequired()]) 
	email = StringField('Email', validators=[DataRequired(),Email()])
	employId = StringField('Employ Id', validators = [DataRequired(), UniqueId])
	password = PasswordField('New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
	confirm  = PasswordField('Repeat Password')
	submit = SubmitField('Sign Up')



