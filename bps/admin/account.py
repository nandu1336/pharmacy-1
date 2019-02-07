from flask import Blueprint,render_template,redirect,flash,url_for,session,request
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
	if request.method == 'GET':
		return render_template("login.html" , form = form , title = "login page" )
	elif request.method == 'POST'and form.validate_on_submit():
		email = request.form['email']
		password = request.form['password'] 
		cursor.execute("SELECT PASSWORD_HASH FROM admin WHERE EMAIL = %s",email)
		passwordHashes = cursor.fetchall()
		if len(passwordHashes) < 1:
			error = "no user found with such details"
		else:
			passwordHash = ''.join(str(Hash) for Hash in passwordHashes)
			stripeSymbols = ['\'','(',')',',','\'',]
			for symbol in stripeSymbols :
				passwordHash = passwordHash.strip(symbol)
			if check_password_hash(passwordHash, password) :
				session['user'] = True
				return render_template("dashboard.html" , title = "Dashboard",session = session)
			else :
				error = "no user found with such details"
		return render_template("login.html", title = "Login" , form = form , error = error)

@Register.route('/register',methods = ['GET','POST'])
def register():
	form = RegisterForm()
	if request.method == 'POST' and form.validate_on_submit():
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
				cursor.execute("INSERT INTO admin VALUES (%s,%s,%s,%s,%s)",(employId,firstName,lastName,email,passwordHash))
				return render_template("login.html")
			else :
				error="Passwords do not match"
				return render_template("register.html",error=error)
			return redirect(url_for('Dashboard.dashboard'))
	return render_template("register.html",title = 'Register',form = form)
