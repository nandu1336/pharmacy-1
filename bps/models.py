import pymysql as db 

host = "localhost"
user = "Project"
password = "password"
database = "pharmacy"
port = 3306

connection = db.connect(host,user,password,database,port)
cursor = connection.cursor()


# 	1. CREATING drug TABLE
Drug = "CREATE TABLE drug(PRODUCT_NAME TEXT NOT NULL,GENERIC_NAME TEXT NOT NULL,SUPPLIER TEXT,DATE_RECEIVED\
 DATE NOT NULL,EXPIRY_DATE DATE NOT NULL,COST_PRICE FLOAT(7,2),MRP FLOAT(7,2) UNSIGNED,STOCK INT NOT NULL\
 ,TYPE ENUM('CAPSULE','TBALET','TONIC','OTHER'),DOSE_IN_MG INT(4) NOT NULL,DRUG_ID VARCHAR(10) PRIMARY KEY NOT NULL);"

# 2. CREATING purchase TABLE
Purchase = "CREATE TABLE purchase(PURCHASE_ID INT PRIMARY KEY NOT NULL auto_increment,PURCHASE_DATE DATE);"

# --3. CREATING patient TABLE
Patient = "CREATE TABLE patient(PATIENT_ID INT(10) UNSIGNED PRIMARY KEY NOT NULL ,NAME TEXT,CONTACT_NO INT(10) UNSIGNED,PLACE TEXT);"

# --4. CREATING sale_transaction TABLE
SaleTransaction = "CREATE TABLE sale_transaction(SALE_ID VARCHAR(10) PRIMARY KEY NOT NULL ,SALE_DATE DATE);"

# --5. CREATING drug_manufacturer TABLE
DrugManufacturer = "CREATE TABLE drug_manufacturer(COMPANY_ID VARCHAR(10) PRIMARY KEY NOT NULL,COMPANY_NAME TEXT);"

# --6. CREATING distributor TABLE
Distributor = "CREATE TABLE distributor(DISTRIBUTOR_ID VARCHAR(10) PRIMARY KEY NOT NULL,CONTACT_NO INT(10) UNSIGNED);"

# --7. CREATING manufactures RELATION
Manufactures = "CREATE TABLE manufactures(COMPANY_ID VARCHAR(10) ,DRUG_ID VARCHAR(10));"

# --8. CREATING prescriptions RELATION 
Prescriptions = "CREATE TABLE prescriptions(PATIENT_ID INT(10) UNSIGNED ,DRUG_ID VARCHAR(10) );"

# --9. CREATING supplies RELATION 
Supplies = "CREATE TABLE supplies(PURCHASE_ID INT ,DISTRIBUTOR_ID VARCHAR(10) ,QUANTITY INT);"

# --10. CREATING sells RELATION 
Sells = "CREATE TABLE sells(DRUG_ID VARCHAR(10) ,PATIENT_ID INT(10) UNSIGNED ,SALE_ID VARCHAR(10) );"

# --11. CREATING admin TABLE
Admin = "CREATE TABLE admin(EMPLOY_ID VARCHAR(10) UNIQUE ,FIRSTNAME VARCHAR(20) ,LASTNAME VARCHAR(20) ,EMAIL VARCHAR(50) UNIQUE ,PASSWORD_HASH CHAR(120) );"

tableNames =[Drug,Purchase,Patient,SaleTransaction,DrugManufacturer,Distributor,Manufactures,Prescriptions,Supplies,Sells,Admin]
for tableName in tableNames:
	cursor.execute(tableName)
	connection.commit()
		

