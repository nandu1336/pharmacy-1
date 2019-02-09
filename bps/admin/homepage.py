from flask import Blueprint,render_template,redirect,flash,url_for,session
from bps.forms import LoginForm
from bps.main.working import Dashboard
from bps.admin.account import Login

Home = Blueprint('Home', __name__)

@Home.route('/')
def index():
	if 'user' in session:
		return redirect(url_for('Dashboard.dashboard'))
	else:
		return redirect(url_for('Login.login'))
		