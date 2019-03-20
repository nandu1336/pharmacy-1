from flask import Blueprint,render_template,redirect,flash,url_for,session,request
from bps.dbase import connection,cursor
from bps.forms import SearchBarForm

Dashboard = Blueprint('Dashboard', __name__)

@Dashboard.route('/dashboard')
def dashboard():
	if 'user' in session:
		return render_template("dashboard.html",title = 'Dashboard')
	else:
		return redirect(url_for('Login.login'))

@Dashboard.route('/stock-Info' , methods = ['POST','GET'])
def stockInfo():
	form = SearchBarForm()
	if 'user' in session :
		if request.method == 'POST' and form.validate_on_submit():
			keyword = request.form['searchFor']
			cursor.execute("SELECT * FROM drug WHERE GENERIC_NAME = %s",keyword)
			productsInfo = cursor.fetchall()
			return render_template('product.html' , form = form, result = productsInfo, title = 'Product')
		else :
			cursor.execute("SELECT * FROM drug;")
			productsInfo = cursor.fetchall()
			return render_template('product.html' , form = form , result = productsInfo, title = 'Product')
	else :
		return redirect(url_for('Login.login'))

@Dashboard.route('/new-sell' , methods = ['POST','GET'])
def newSell():
	form = SearchBarForm()
	if 'user' in session :
		return render_template('sell.html' , form = form, result = newSell)
	else :
		return redirect(url_for('Login.login'))
@Dashboard.route('/new-entry' , methods = ['POST','GET'])
def newEntry():
	form = SearchBarForm()
	if 'user' in session :
		return render_template('newEntry.html' , form = form, result = newEntry)
	else :
		return redirect(url_for('Login.login'))