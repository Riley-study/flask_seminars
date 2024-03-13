# Создать форму для регистрации пользователей на сайте. Форма должна содержать поля
# "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться". При отправке формы
# данные должны сохраняться в базе данных, а пароль должен быть зашифрован.

from flask import Flask, render_template, request, redirect
from flask_wtf import CSRFProtect

from models import db, User
from forms import RegisterForm
from werkzeug.security import generate_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_users_hw.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/')
def index():
    return redirect('/register/')
@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data
        # добавляем хеширование пароля, в бд сохранится хэш вариант
        hashed_password = generate_password_hash(password)
        user = User(firstname=firstname, lastname=lastname, email=email, password=hashed_password)
        # записываем данные в бд
        db.session.add(user)
        db.session.commit()
        return f'Вы зарегистрированы'
    return render_template('register.html', form=form)



# для проверки по пути /users/ можно также посмотреть сколько пользователей в базе
@app.route('/users/', methods=['GET', 'POST'])
def add_users():
    users = User.query.all()
    return f'{list(users)}'

