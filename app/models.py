from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    code = db.Column(db.String(10), unique=True)
    students = db.relationship('Student', backref='department', lazy=True)
    staff = db.relationship('Staff', backref='department', lazy=True)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128))
    barcode = db.Column(db.String(128), unique=True)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(50))
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
