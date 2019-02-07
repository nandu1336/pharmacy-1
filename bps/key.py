from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,Email,InputRequired,EqualTo
import keyboard as kb
import pymysql as db

host = "localhost"
user = "nandu"
password = "password"
database = "pharmacy"
port = 3306

# def findId():
# 	cursor.execute("SELECT FIRSTNAME FROM Admin WHERE EMPLOY_ID= {}".format(string))
# 	rows =cursor.fetchall()
# 	if len(rows) > 0:
# 		print("Id already exists,enter some other id.")

connection = db.connect(host,user,password,database,port)
cursor = connection.cursor()
# string = input("enter you employId:")
# print("press space to continue")
# kb.wait('space')
# if kb.is_pressed('space'):
# 	findId()
	
firstName = "akshay kumar"
lastName = "talluri"
email = "talluri.akshaykukmar@gmail.com"
employId = "15532"
passwordHash = "1231aalakoaldsfxcfccaklr98hacjfo9ahbKNfdosacvhabe3ul9oh"

entry  =  "INSERT INTO admin VALUES ({},{},{},{},{}).format(employId,firstName,lastName,email,passwordHash)"
cursor.execute(entry)

	# 		if res > 0:
	# 			raise ValidationError('An admin with this EMPLOY_ID already exists!!')

	# firstName = StringField('Firstname', validators=[DataRequired()]) 
	# lastName = StringField('Lastname', validators=[DataRequired()]) 
	# email = StringField('Email', validators=[DataRequired(),Email()])
	# employId = StringField('Employ Id', validators = [DataRequired(), UniqueId])
	# password = PasswordField('New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
	# confirm  = PasswordField('Repeat Password')
	# submit = SubmitField('Sign Up')