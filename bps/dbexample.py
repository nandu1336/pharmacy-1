import pymysql as db

host = "localhost"
user = "Project"
password = "password"
database = "pharmacy"
port = 3306

connection = db.connect(host,user,password,database,port)
cursor = connection.cursor()

# creating a table
SaleTransaction = "CREATE TABLE sale_transaction(SALE_ID VARCHAR(10) PRIMARY KEY NOT NULL ,SALE_DATE DATE);"
cursor.execute(SaleTransaction)
# commiting request to reflect the changes made
cursor.commit()

# inserting into table 
insert = "INSERT INTO sale_transaction VALUES ("15306","30-01-2019");"
cursor.commit()

# querying the database
query = "SELECT * FROM sale_transaction;"
cursor.execute(query);
queryResults = cursor.fectall()