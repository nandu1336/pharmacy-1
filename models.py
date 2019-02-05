from bps import db

class User(db.Model):
	__tablename__ = "User"
	id = db.Column('id',db.Integer,primary_key = True)
	admin_username = db.Column('username',db.String(64),index = True,unique = True)
	admin_firstname = db.Column('firstname',db.String(64),unique = True)
	admin_email = db.Column('email',db.String(120),index = True,unique = True)
	admin_password_hash = db.Column('password',db.String(128))
	admin_contact = db.Column('contact',db.String(10),unique = True)

class Drug(db.Model):
	__tablename__ = "Drug"
	id = db.Column('id',db.Integer,primary_key = True)
	drug_name = db.Column('drug_name',db.String(64),index = True,unique = True)
	drug_type = db.Column('drug_type',db.String(64),unique = True)
	drug_MRP = db.Column('drug_MRP',db.Decimal(120),index = True,unique = True)
	drug_cost = db.Column('drug_cost',db.Decimal(128))
	drug_expiry_date = db.Column('drug_expiry_date',db.Date,unique = True)

