from flask import Blueprint,render_template,redirect,flash,url_for,session,request
from bps.dbase import connection,cursor
from bps.forms import SearchBarForm,NewEntry
import datetime

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
		if request.method == 'POST' :
			keyword = request.form['searchFor']
			classBy = request.form['select']
			cursor.execute("SELECT * FROM drug WHERE GENERIC_NAME = %s",keyword)
			if(classBy == "GENERIC_NAME"):
				cursor.execute("SELECT * FROM drug WHERE GENERIC_NAME = %s",keyword)
			elif(classBy == "SUPPLIER"):
				cursor.execute("SELECT * FROM drug WHERE SUPPLIER = %s",keyword)
			elif(classBy == "EXPIRY_DATE"):
				cursor.execute("SELECT * FROM drug WHERE EXPIRY_DATE >= %s",keyword)
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
		keyword = "Dolo 360"
		cursor.execute("SELECT * FROM drug WHERE PRODUCT_NAME = %s",keyword)
		result = cursor.fetchall()
		quantity = 1
		amount = 10
		return render_template('sell.html' , form = form, result=result, quantity=quantity, amount=amount)
	else :
		return redirect(url_for('Login.login'))
@Dashboard.route('/new-entry' , methods = ['POST','GET'])
def newEntry():
	form = NewEntry()
	if 'user' in session :
		if request.method == 'POST' and form.validate_on_submit():
			productName = request.form['productName']
			genericName = request.form['genericName']
			supplier = request.form['supplier']
			receivedDate = request.form['dateReceived']
			expiryDate = request.form['expiryDate']
			costPrice = request.form['costPrice']
			MRP = request.form['MRP']
			stock = request.form['stock']
			medicineType = request.form['medicineType']
			dose = request.form['dose']
			drugId = request.form['drugId']

			if cursor.execute("INSERT INTO drug VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",\
				(productName,genericName,supplier,receivedDate,expiryDate,costPrice,MRP,stock,medicineType,dose,drugId)):
				connection.commit()
				error =  "product details entered successfully"
			else:
				error = "could not enter product details."
			return render_template('newEntry.html', form = form , error = error)
		return render_template('newEntry.html' , form = form)
	else :
		return redirect(url_for('Login.login'))


@Dashboard.route('/sales-history' , methods = ['POST','GET'])
def salesHistory():
	form = NewEntry()
	if 'user' in session :
		return render_template('invoices.html' , form = form)
	else :
		return redirect(url_for('Login.login'))
