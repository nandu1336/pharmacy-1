from flask import Blueprint,render_template,redirect,flash,url_for
from bps.forms import LoginForm

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
		flash("you r successfully registered")
		return redirect(url_for('dashboard'))
	return render_template("login.html",title = 'Login',form = form)
