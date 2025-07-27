from flask import Blueprint, render_template, request, redirect, url_for
from app.models import db, Student, Department
from werkzeug.security import generate_password_hash
import barcode
from barcode.writer import ImageWriter
import os

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/register-student', methods=['GET', 'POST'])
def register_student():
    if request.method == 'POST':
        name = request.form['name']
        dept_id = request.form['department']
        email = name.replace(' ', '').lower() + "@college.edu"
        password = generate_password_hash("AutoPass123")

        student = Student(name=name, email=email, password=password, department_id=dept_id)
        db.session.add(student)
        db.session.commit()

        # Generate barcode
        barcode_data = f"STU{student.id:05d}"
        student.barcode = barcode_data
        db.session.commit()

        code128 = barcode.get('code128', barcode_data, writer=ImageWriter())
        filepath = f"app/static/barcodes/{barcode_data}.png"
        code128.save(filepath)

        return redirect(url_for('main.view_students'))

    departments = Department.query.all()
    return render_template('register_student.html', departments=departments)

@main.route('/students')
def view_students():
    students = Student.query.all()
    return render_template('student_list.html', students=students)
