from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(20), unique=True)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150), nullable=False)
    dob = db.Column(db.Date)
    contact = db.Column(db.String(20))
    address = db.Column(db.Text)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(200))  # Store hashed password
    barcode_data = db.Column(db.String(200), unique=True)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150), nullable=False)
    contact = db.Column(db.String(20))
    role = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(200))
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
