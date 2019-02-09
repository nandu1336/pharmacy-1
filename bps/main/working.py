from flask import Blueprint,render_template,redirect,flash,url_for,session,request

Dashboard = Blueprint('Dashboard', __name__)

@Dashboard.route('/dashboard')
def dashboard():
	if 'user' in session:
		return render_template("dashboard.html",title = 'Dashboard')
	else:
		return redirect(url_for('Login.login'))

@Dashboard.route('/stock-Info')
def stockInfo():
	if 'user' in session :
		if request.method == 'POST' and form.validate_on_submit():
			return render_template('product.html')
		else :
			return render_template('product.html')
	else :
		return redirect(url_for('Login.login'))

