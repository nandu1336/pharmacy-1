from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# class RegisterForm(FlaskForm):
# 	firstname = StringField('Firstname', validators=[DataRequired(),Email()]) 
# 	lasttname = StringField('Firstname', validators=[DataRequired(),Email()]) 
# 	email = StringField('Email', validators=[DataRequired(),Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
#     submit = SubmitField('Sign In')
