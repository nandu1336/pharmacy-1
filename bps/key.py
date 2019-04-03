from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,Email,InputRequired,EqualTo
from werkzeug.security import generate_password_hash,check_password_hash
import pymysql as db
import datetime as dt 

host = "localhost"
user = "Project"
password = "password"
database = "pharmacy"
port = 3306

# def findId():
# 	cursor.execute("SELECT FIRSTNAME FROM Admin WHERE EMPLOY_ID= {}".format(string))
# 	rows =cursor.fetchall()
# 	if len(rows) > 0:
# 		print("Id already exists,enter some other id.")

connection = db.connect(host,user,password,database,port)
cursor = connection.cursor()
supplier = "nandu"
cursor.execute("SELECT supplier_Id from supplier WHERE company_name= %s",(supplier))
suppliers = cursor.fetchall()
if len(suppliers) > 0:
	print("fine")
else:
	print("no match found")
# for everysupplier in suppliers:
	print(everysupplier[0])
# if supplier.length == 0:
# 	print()
# for everySupplier in suppliers:
# 	for i in everySupplier:
# 		if i != supplier:
# 			noSupplierFound = True
# 		else:
# 			noSupplierFound = False
# 			break
# if noSupplierFound :
# 	print("no supplier found with this name")
# else:
# 	print("supplier found")
# print(noSupplierFound)
# cursor.execute("SELECT expiry_date,drug_Id  FROM drug")
# expiryDates = cursor.fetchall()
# expiresSoon = []

# for expiryDate in expiryDates:
# 		today =  dt.date.today()
# 		daysLeft = str(expiryDate[0]-today)
# 		daysLeft = int(daysLeft.split(' ')[0])
		
# 		print("time gap",daysLeft)

# 		if(daysLeft < 30):
# 			print("medicine expires in ",daysLeft,"days")
# 			expiresSoon.append(expiryDate[1])

# expiresSoon = len(expiresSoon)
# if expiresSoon > 0 :
	# print("check alerts for more info.")
# keyword = "val"
# cursor.execute("SELECT * FROM drug WHERE PRODUCT_NAME LIKE %s%",keyword)
# result = cursor.fetchall()
# for i in result:
# 	print(i)
# choice = []
# newArray = []
# cursor.execute("SELECT PRODUCT_NAME FROM drug")
# output = cursor.fetchall()
# for everyInput in output:
# 	choice.append(everyInput[0])
# for i in choice:
# 	result = "("+i+","+i+")"
# 	newArray.append(result)
# print(newArray)
# query using parameterized arguments to the execute function 

# keyword = "SOMExyz"
# classBy = "GENERIC_NAME"
# cursor.execute("SELECT * FROM drug WHERE SUPPLIER = %s",keyword)
# outputs = cursor.fetchall()
# for output in outputs:
# 	for everyInput in output :
# 		print(everyInput)
# 	print("\n")


# productName = "lopermide hydrochloride"
# genericName = "L-par"
# supplier = "nandu"
# receivedDate = "2019-03-26"
# expiryDate = "2021-03-06"
# costPrice = "20"
# MRP = "30"
# stock = "250"
# medicineType = "1"
# dose = "2"
# drugId = "l-par2"

# query = "INSERT INTO drug VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(productName,genericName,supplier,receivedDate,expiryDate,costPrice,\
# MRP,stock,medicineType,dose,drugId)

# if cursor.execute("INSERT INTO drug VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(productName,genericName,supplier,receivedDate,expiryDate,costPrice,MRP,stock,medicineType,dose,drugId)):
# 	connection.commit()
# 	print("successfully iserted and changes are reflected in the database:")
# 	var = input("press Y to see the drug table:")
# 	if var =='y'or var == 'Y':
# 		cursor.execute("SELECT * FROM drug;")
# 		results = cursor.fetchall()
# 		for result in results:
# 			print(result)
			# print("\n")

# string = input("enter you employId:")
# print("press space to continue")
# kb.wait('space')
# if kb.is_pressed('space'):
# 	findId()
	
# firstName = "akshay kumar"
# lastName = "talluri"
# email = "talluri.akshaykukmar@gmail.com"
# employId = "15532"
# passwordHash = "1231aalakoaldsfxcfccaklr98hacjfo9ahbKNfdosacvhabe3ul9oh"

# entry  =  "INSERT INTO admin VALUES ({},{},{},{},{}).format(employId,firstName,lastName,email,passwordHash)"
# cursor.execute(entry)

# INSERTING A DEFAULT ADMIN VALUES INTO THE DATABASE
# password = generate_password_hash('admin')
# cursor.execute("INSERT INTO admin VALUES ('521' , 'admin' , 'baskar pharmacy', 'admin@baskar.com' , %s)",password)
# connection.commit()


# cursor.execute("SELECT PASSWORD_HASH,FIRSTNAME FROM admin")
# res = cursor.fetchall()
# print(res[0][0],res[0][1])
# print(res)
# email = 'admin@baskar.com'
# password = 'admin'
# cursor.execute("SELECT PASSWORD_HASH FROM admin WHERE EMAIL = %s",email)
# passwordHashes = cursor.fetchall()
# if len(passwordHashes) < 1:
# 	error = "FAILED AT EMAIL FIELD"
# 	print(error)
# else:
# passwordHash = ''.join(str(Hash) for Hash in res)

# stripeSymbols = ['\'','(',')',',','\'',]
# for symbol in stripeSymbols :
# 	passwordHash = passwordHash.strip(symbol)

# passwordHash = res[0][0]
# print(passwordHash)
# if passwordHash == str(generate_password_hash('admin')):
# 	print("your details are verified")
# else:
# 	print("you entered wrong details")
# if check_password_hash(passwordHash, 'admin') :
# 	print("your details are verified")
# else:
# 	print("entered wrong details")


# cursor.execute("SELECT PASSWORD_HASH FROM admin WHERE EMAIL = %s",email)
# res = cursor.fetchall()
# passwordHash = ''.join(str(e) for e in res)
# stripeSymbols = ['\'','(',')',',','\'',]
# for symbol in stripeSymbols :
# 	passwordHash = passwordHash.strip(symbol)
# print(passwordHash)

# if passwordHash == "admin":
# 	print("you entered right password")
# if check_password_hash(passwordHash, "admin") :
	# print("your password is correct and verified using second method")

	# 		if res > 0:
	# 			raise ValidationError('An admin with this EMPLOY_ID already exists!!')

	# firstName = StringField('Firstname', validators=[DataRequired()]) 
	# lastName = StringField('Lastname', validators=[DataRequired()]) 
	# email = StringField('Email', validators=[DataRequired(),Email()])
	# employId = StringField('Employ Id', validators = [DataRequired(), UniqueId])
	# password = PasswordField('New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
	# confirm  = PasswordField('Repeat Password')
	# submit = SubmitField('Sign Up')

	# INSERTING VALUES INTO THE DRUG TABLE:
# cursor.execute("INSERT INTO DRUG VALUES ('SODIUM VALPORATE HYDROXIDE','VALPHYARIN 250','SOMExyz','2019-02-09','2022-01-23',\
# 	'150','198','300',2,'250','SI200' ), ('SODIUM VALPORATE','VALPARIN 200','SOMExyz','2019-02-09','2022-01-23',\
# 	'75','98','700',2,'200','SV200' ),('IBUPROFIN','BRUFIN 200','SOMEXyz','2019-02-09','2022-01-23',\
# 	'45','32','1200',2,'200','IB200' );")
# connection.commit()
# cursor.execute("SELECT * FROM drug;")
# productsInfo = cursor.fetchall()
# for p in productsInfo:
# 	for i in range(0,10):
# 		print(p[i])