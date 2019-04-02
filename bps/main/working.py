from flask import Blueprint,render_template,redirect,flash,url_for,session,request
from bps.dbase import connection,cursor
from bps.forms import SearchBarForm,NewEntry,ChoseProducts,QuerySales
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
	form = ChoseProducts()
	if 'user' in session :
		if request.method == 'POST':
			keyword = request.form['search']
			quantity = request.form['quantity']
			cursor.execute("SELECT PRODUCT_NAME,GENERIC_NAME,MRP FROM drug WHERE PRODUCT_NAME LIKE %s",keyword)
			productInfo = cursor.fetchone()
			amount = productInfo[0][2]*quantity
			if cursor.execute("INSERT INTO purchase VALUES (%s,%s,%s,%s,%s)",\
				(productInfo[0],productInfo[1],productInfo[2],quantity,amount)):
				connection.commit()
				error =  "product details entered successfully"
			else:
				error = "could not enter product details."
			cursor.execute("SELECT * FROM purchase")
			salesInfo = cursor.fetchall()
			return render_template('sell.html' , form = form , salesInfo = salesInfo)
			
		return render_template('sell.html' , form = form )
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
	form = QuerySales()
	if 'user' in session :
		if request.method == 'POST' and form.validate_on_submit():
			StartDate = request.form['startDate']
			EndDate = request.form['endDate']
			cursor.execute("SELECT * FROM sale_transaction where SALE_DATE>=%s AND SALE_DATE<=%s",(StartDate,EndDate))
			result = cursor.fetchall()
			return render_template('invoices.html' , form = form, result=result)
		return render_template('invoices.html' , form = form)
	else :
		return redirect(url_for('Login.login'))

@Dashboard.route('/suppliers-info' , methods = ['POST','GET'])
def suppliersInfo():
	if 'user' in session :
		cursor.execute("SELECT * FROM supplier")
		suppliersInfo = cursor.fetchall()
		return render_template('suppliers.html', result=suppliersInfo)
	else :
		return redirect(url_for('Login.login'))
# changed nothing but added something