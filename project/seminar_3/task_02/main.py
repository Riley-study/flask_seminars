import random

from flask import Flask, render_template
from task_02.models import db, Book, BookAuthor, Author

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_books.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-book")
def add_data():
    for i in range(1, 10):
        book = Book(
            name=f'book{i}',
            year=random.randint(1800, 2024),
            count=random.randint(100, 1000)
        )
        db.session.add(book)
    for i in range(1, 15):
        author = Author(
            firstname=f'name{i}',
            lastname=f'lastname{i}',
        )
        db.session.add(author)
    for i in range(1, 15):
        book_author = BookAuthor(
            book_id=random.randint(1,9),
            author_id=random.randint(1,14),
        )
        db.session.add(book_author)
    db.session.commit()
    print('books add')


@app.get('/')
def get_book():
    books = Book.query.all()
    context = {'books': books}
    return render_template('books.html', **context)
