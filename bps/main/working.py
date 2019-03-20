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
			classBy = request.form['classBy']
			cursor.execute("SELECT * FROM drug WHERE %s = %s",(classBy,keyword))
			productsInfo = cursor.fetchall()
			return render_template('product.html' , form = form, result = productsInfo, title = 'Product')
		else :
			classBy = "GENERIC_NAME"
			keyword = "valparin 200"
			cursor.execute("SELECT * FROM drug WHERE %s = %s",(classBy,keyword))
			# cursor.execute("SELECT * FROM drug;")
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
