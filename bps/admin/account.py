from flask import Blueprint,render_template,redirect,flash,url_for,session,request
from bps.forms import LoginForm,RegisterForm
from werkzeug.security import generate_password_hash,check_password_hash
from bps.dbase import connection,cursor
import datetime

Login = Blueprint('Login', __name__)
Register = Blueprint('Register',__name__)

# Login view 
@Login.route('/login',methods = ['GET','POST'])
def login():
	if 'user' in session:
		session.pop('user',None)
	form = LoginForm()
	if request.method == 'POST' and form.validate_on_submit():
		email = request.form['email']
		password = request.form['password'] 
		cursor.execute("SELECT PASSWORD_HASH,FIRSTNAME FROM admin WHERE EMAIL = %s",email)
		resultRows = cursor.fetchall()

		if len(resultRows) == 1:
			passwordHash = resultRows[0][0]
			if check_password_hash(passwordHash, password) :
				session['user'] = resultRows[0][1]
				return render_template("dashboard.html" , title = "Dashboard",session = session)
			else :
				error = "no user found with such details"
		else:
			error = "no user found with such details"
		return render_template("login.html", title = "Login" , form = form , error = error)

	return render_template("login.html" , form = form , title = "Login" )


# Register view
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
			return redirect(url_for('register'))
		else :
			if password == confirm:
				passwordHash=generate_password_hash(password)
				cursor.execute("INSERT INTO admin VALUES (%s,%s,%s,%s,%s)",(employId,firstName,lastName,email,passwordHash))
				connection.commit()
				return redirect(url_for('Login.login'))
			else :
				error="Passwords do not match"
				return render_template("register.html",error=error)
			return redirect(url_for('Dashboard.dashboard'))
	return render_template("register.html",title = 'Register',form = form)
