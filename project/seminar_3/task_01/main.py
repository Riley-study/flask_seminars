import random

from flask import Flask, render_template
from task_01.models import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-student")
def add_data():
    for i in range(1, 4):
        faculty = Faculty(name=f'faculty{i}')
        db.session.add(faculty)
    for i in range(1, 11):
        student = Student(
            firstname=f'name{i}',
            lastname=f'lastname{i}',
            age=random.randint(17, 23),
            gender=random.choice(['m', 'f']),
            group=random.randint(1, 4),
            id_faculty=random.randint(1, 3)
        )
        db.session.add(student)
    db.session.commit()
    print('students add')


@app.get('/')
def get_student():
    students = Student.query.all()
    context = {'students': students}
    return render_template('books.html', **context)
