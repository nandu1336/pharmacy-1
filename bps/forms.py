from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField , SelectField , RadioField , FloatField , IntegerField
from wtforms.validators import DataRequired,Email , InputRequired , EqualTo,Length , NumberRange
from wtforms.fields.html5 import DateField , EmailField
import datetime
from bps.dbase import connection,cursor

class LoginForm(FlaskForm):
    email = EmailField('Email', validators = [DataRequired(),Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Sign In')
    rememberMe = BooleanField('Remember Me')

class RegisterForm(FlaskForm):
	firstName = StringField('Firstname', validators = [DataRequired()]) 
	lastName = StringField('Lastname', validators = [DataRequired()]) 
	email = EmailField('Email', validators = [DataRequired(),Email()])
	employId = StringField('Employ Id', validators = [DataRequired()])
	password = PasswordField('New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match'), Length(min=8, message = 'Password should contain minimum eight characters')])
	confirm  = PasswordField('Repeat Password', [InputRequired(),Length(min=8, message = 'Password should contain minimum eight characters')])
	submit = SubmitField('Create Account')

# this is a class to add a search box in the products info. page.
# main usage in : bps>main>working>productInfo
class SearchBarForm(FlaskForm):
	searchFor = StringField('Search', validators = [DataRequired()])
	submit = SubmitField('Search')
	datePicker = DateField('Date Picker',format = "%Y-%m-%d" ,validators = [DataRequired()] )
	select =  SelectField('Search from', choices = [('GENERIC_NAME','GENERIC_NAME'),('EXPIRY_DATE','EXPIRY_DATE'),('SUPPLIER','SUPPLIER')])

class NewEntry(FlaskForm):
	productName = StringField('Productname',validators = [DataRequired()])
	genericName = StringField('Genericname',validators = [DataRequired()])
	supplier = StringField('Supplier',validators = [DataRequired()])
	dateReceived = DateField('Date received', format = "%Y-%m-%d" , default = datetime.datetime.today , validators = [DataRequired()])
	expiryDate = DateField('Expiry date', format = "%Y-%m-%d" , validators = [DataRequired()])
	costPrice = FloatField('Cost price',validators = [DataRequired() , NumberRange(min=0, message='this field cannot be negative')])
	MRP = FloatField('MRP',validators = [DataRequired() , NumberRange(min=0, message='this field cannot be negative')])
	stock = IntegerField('Stock',validators = [DataRequired(), NumberRange(min=0, message='this field cannot be negative')])
	medicineType  = SelectField('Type', choices = [('default','Type'),('1','capsule'),('2','tablet'),('3','tonic'),('4' , 'other')] , validators = [DataRequired()])
	dose = IntegerField('Dose',validators = [DataRequired(), NumberRange(min=0, message='this field cannot be negative')])
	drugId = StringField('Drug Id',validators = [DataRequired()])
	submit = SubmitField('Submit')

class ChoseProducts(FlaskForm):
	# choices = []
	# cursor.execute("SELECT PRODUCT_NAME FROM drug")
	# queryResult = cursor.fetchall()
	# for result in queryResult:
	# 	choices.append(result)
	# choose = SelectField('choose' , choices = choices )
	search = StringField('product name' , validators = [DataRequired()])
	quantity = IntegerField('quantity' , validators = [DataRequired(), NumberRange(min=0, message='this field cannot be negative')])
	submit = SubmitField('Add item')

class QuerySales(FlaskForm):
	startDate = DateField('Start date', format = "%Y-%m-%d" , validators = [DataRequired()])
	endDate = DateField('End date', format = "%Y-%m-%d" , validators = [DataRequired()])
	submit = SubmitField('Search')

class finishSale(FlaskForm):
	cancel = SubmitField('Cancel')
	confirm = SubmitField('Confirm Sale')