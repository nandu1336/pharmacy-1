from flask import Blueprint,render_template,redirect,flash,url_for
from bps.forms import LoginForm,RegisterForm
from werkzeug.security import generate_password_hash,check_password_hash
import datetime
import pymysql as db

host = "localhost"
user = "Project"
password = "password"
database = "pharmacy"
port = 3306

connection = db.connect(host,user,password,database,port)
cursor = connection.cursor()

Login = Blueprint('Login', __name__)
Register = Blueprint('Register',__name__)

@Login.route('/login',methods = ['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash("you r successfully logged in")
		return redirect(url_for('Home.index'))
	return render_template("login.html",title = 'Login',form = form)

@Register.route('/register',methods = ['GET','POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		firstName = request.form['firstName'] 
		lastName = request.form['lastName'] 
		employId = request.form['employId'] 
		email = request.form['email'] 
		password = request.form['password'] 
		confirm = request.form['confirm']

		cursor.execute("SELECT FIRSTNAME FROM admin WHERE EMPLOY_ID = {}".format(employId))
		noOfUsers = cursor.fetchall()
		if len(noOfUsers) > 0:
			error="A user with this Roll Number/Email already exists."
			return render_template("register.html", title = 'Register', form = form , error=error)
		else :
			if password == confirm:

				passwordHash=generate_password_hash(password)
				entry  =  "INSERT INTO admin VALUES ({0},{1},{2},{3},{4}).format(employId,firstName,lastName,email,passwordHash)"
				cursor.execute(entry)
				return render_template("login.html")
			else :
				error="Passwords do not match"
				return render_template("regStudent.html",error=error)
			return redirect(url_for('Dashboard.dashboard'))
	return render_template("register.html",title = 'Register',form = form)
