from flask import Blueprint,render_template,redirect,flash,url_for,session,request
from bps.dbase import connection,cursor
from bps.forms import SearchBarForm,NewEntry,ChoseProducts,QuerySales,finishSale
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
	cursor = connection.cursor()
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
			cursor.close()
			return render_template('product.html' , requestFrom = " dashboard" ,  form = form, result = productsInfo, title = 'Product')
		else :
			cursor.execute("SELECT * FROM drug;")
			productsInfo = cursor.fetchall()
			cursor.close()
			return render_template('product.html' , requestFrom = " dashboard" , form = form , result = productsInfo, title = 'Product')
	else :
		return redirect(url_for('Login.login'))

@Dashboard.route('/new-sell' , methods = ['POST','GET'])
def newSell():
	cursor = connection.cursor()
	form = ChoseProducts()
	if 'user' in session :
		cursor.execute("SELECT * FROM purchase")
		salesInfo = cursor.fetchall()
		if request.method == 'POST':
			keyword = request.form['search']
			quantity = request.form['quantity']
			cursor.execute("SELECT PRODUCT_NAME,GENERIC_NAME,MRP FROM drug WHERE PRODUCT_NAME LIKE %s",keyword)
			productInfo = cursor.fetchone()
			if productInfo != None :
				cursor.execute("SELECT PRODUCT_NAME FROM purchase WHERE PRODUCT_NAME LIKE %s",keyword)
				alreadyPresent = cursor.fetchone()
				if alreadyPresent == None :
					amount = float(productInfo[2])*float(quantity)
					if cursor.execute("INSERT INTO purchase VALUES (%s,%s,%s,%s,%s)",\
						(productInfo[0],productInfo[1],productInfo[2],quantity,amount)):
						connection.commit()
						error =  "product details entered successfully"
					else:
						error = "could not enter product details."
					cursor.execute("SELECT * FROM purchase")
					salesInfo = cursor.fetchall()
					return render_template('sell.html' , form = form , requestFrom = " dashboard" , salesInfo = salesInfo)
				else :
					error = "The medicine already exists in the list."
					return render_template('sell.html' , form = form , requestFrom = " dashboard", error=error, salesInfo=salesInfo)
			else :
				error = "The medicine does not exist."
				return render_template('sell.html' , form = form , requestFrom = " dashboard", error=error, salesInfo=salesInfo)
		
		return render_template('sell.html' , requestFrom = " dashboard" , form = form, salesInfo=salesInfo)
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
		return render_template('newEntry.html' , requestFrom = " dashboard" , form = form)
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
		return render_template('invoices.html' , requestFrom = " dashboard" , form = form)
	else :
		return redirect(url_for('Login.login'))

@Dashboard.route('/suppliers-info' , methods = ['POST','GET'])
def suppliersInfo():
	if 'user' in session :
		cursor.execute("SELECT * FROM supplier")
		suppliersInfo = cursor.fetchall()
		return render_template('suppliers.html', requestFrom = "dashboard" , result=suppliersInfo)
	else :
		return redirect(url_for('Login.login'))
# changed nothing but added something

# NEW SELL ---> CHECK NOW ---> CONFIRM
@Dashboard.route('/confirm-sale' , methods = ['POST','GET'])
def confirmSale():
	cursor = connection.cursor()
	form = finishSale()
	if 'user' in session:
		cursor.execute("SELECT * FROM purchase")
		purchaseInfo = cursor.fetchall()
		totalAmount=0
		if purchaseInfo != None :
			for i in range(len(purchaseInfo)):
				totalAmount = totalAmount + purchaseInfo[i][4]
<<<<<<< HEAD
		if request.method == 'POST' :
			if request.form['operation'] == "cancel" :
				if cursor.execute("DELETE FROM purchase") :
					connection.commit()
				return render_template("dashboard.html", requestFrom = "dashboard", title = 'Dashboard')
			else :
				return render_template("confirmSale.html", requestFrom = "dashboard", title = 'Confirm Sale', purchaseInfo = purchaseInfo, totalAmount = totalAmount, form = form)

=======
>>>>>>> 92d040a0860a06c3dd5df489f2488b1d80b9b908
		return render_template("confirmSale.html", requestFrom = "dashboard", title = 'Confirm Sale', purchaseInfo = purchaseInfo, totalAmount = totalAmount, form = form)
	else:
		return redirect(url_for('Login.login'))


@Dashboard.route('/cancel-transaction' , methods = ['POST','GET'])
def cancelTransaction():
	cursor = connection.cursor()
	if 'user' in session:
		if cursor.execute("DELETE FROM PURCHASE") :
			connection.commit()
			error = "Purchase successfully Canceled"
		return render_template("dashboard.html",title = 'Dashboard',requestFrom = "dashboard", error = error)
	else:
		return redirect(url_for('Login.login'))



@Dashboard.route('/confirm-transaction' , methods = ['POST','GET'])
def confirmTransaction():
	cursor = connection.cursor()
	if 'user' in session :
		cursor.execute("SELECT * FROM purchase")
		purchaseInfo = cursor.fetchall()
		boolVal = 1
		for row in purchaseInfo :
			cursor.execute("SELECT * FROM drug where PRODUCT_NAME=%s",row[0])
			drugX = cursor.fetchone()
			if row[3] > drugX[7] : #If quantity of purchase is more than what we have in inventory
				boolVal = 0
		if boolVal == 1 :
			cursor.execute("SELECT * FROM sale_transaction")
			salesInfo = cursor.fetchall()
			totalSales = len(salesInfo)
			saleId = totalSales+1
			if cursor.execute("INSERT INTO sale_transaction VALUES (%s,now(),%s)",\
					(saleId,row[4])):
				connection.commit()
				error =  "Transaction successfully completed"
			for row in purchaseInfo :
				cursor.execute("SELECT * FROM drug where PRODUCT_NAME=%s",row[0])
				drugX = cursor.fetchone()
				remainingStock = drugX[7] - row[3]
				if cursor.execute("UPDATE drug SET STOCK=%s WHERE PRODUCT_NAME=%s",(remainingStock,row[0])):
					connection.commit()
			if cursor.execute("DELETE FROM PURCHASE") :
				connection.commit()
			form = QuerySales()
			return render_template("invoices.html",title = 'Invoices',requestFrom = "dashboard", error = error, form = form)
		else :
			error = "Not enough stock in the inventory"
			form = ChoseProducts()
			return render_template("sell.html",title = 'Sell',requestFrom = "dashboard", error = error, form = form)
	else :
		return redirect(url_for('Login.login'))