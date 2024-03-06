# Создать страницу, на которой будет кнопка "Нажми меня", при нажатии будет переход на другую страницу с
# приветствием пользователя по имени.
from pathlib import PurePath, Path
import logging

from markupsafe import escape
from flask import Flask, render_template, request, abort, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='templates')

app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/next/')
def next_page():
    return 'Привет, Вася'


# Создать страницу, на которой будет изображение и ссылка на другую страницу, на которой будет отображаться форма
# для загрузки изображений.

@app.route('/load_image/', methods=['GET', 'POST'])
def load_image():
    context = {'task': 'task_2'}
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {escape(file_name)} загружен на сервер"
    return render_template('page1.html', **context)


# Создать страницу, на которой будет форма для ввода логина и пароля
# При нажатии на кнопку "Отправить" будет произведена проверка соответствия логина и пароля и переход на
# страницу приветствия пользователя или страницу с ошибкой.
@app.route('/authorization/', methods=['GET', 'POST'])
def authorization():
    context = {'task': 'task_3'}
    login = {
        'auth_email': '1@mail.ru',
        'auth_pass': '123'
    }
    if request.method == 'POST':
        auth_email = request.form.get('auth_email')
        auth_pass = request.form.get('auth_pass')
        if auth_email == login['auth_email'] and auth_pass == login['auth_pass']:
            return f"Вход с почты {escape(auth_email)} выполнен"
        else:
            return "Error"
    return render_template('authorization.html', **context)


# Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов в тексте и переход на страницу с результатом.

@app.route('/counter/', methods=['GET', 'POST'])
def counter():
    context = {'task': 'task_4'}
    if request.method == 'POST':
        text = request.form.get('text')
        return f"Количество слов: {len(text.split())}"
    return render_template('counter.html', **context)


# Создать страницу, на которой будет форма для ввода двух чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить". При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с результатом.

@app.route('/calculate/', methods=['GET', 'POST'])
def calculate():
    context = {'task': 'task_5'}
    if request.method == 'POST':
        number_1 = request.form.get('number_1')
        number_2 = request.form.get('number_2')
        operation = request.form.get('operation')
        match operation:
            case 'add':
                return f'{int(number_1) + int(number_2)}'
            case 'subtract':
                return f'{int(number_1) - int(number_2)}'
            case 'multiply':
                return f'{int(number_1) * int(number_2)}'
            case 'divide':
                if number_2 == '0':
                    return f"Нельзя делить на ноль"
                return f'{int(number_1) / int(number_2)}'
    return render_template('calculate.html', **context)


# Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.

@app.errorhandler(403)
def page_not_found(e):
    # logger.warning(e)
    context = {
        'title': 'Доступ запрещен по возрасту',
        'url': request.base_url
    }
    return render_template('403.html', **context), 403


@app.route('/age/', methods=['GET', 'POST'])
def age():
    context = {'task': 'task_6'}
    MIN_AGE = 18
    if request.method == 'POST':
        name = request.form.get('name')
        age_ = request.form.get('age')
        if int(age_) > MIN_AGE:
            return f'Приветствую, {name}! Вы вошли на сайт'
        abort(403)
    return render_template('age.html', **context)


# Создать страницу, на которой будет форма для ввода числа и кнопка "Отправить"
# При нажатии на кнопку будет произведено перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.

@app.route('/square/', methods=['GET', 'POST'])
def square():
    context = {'task': 'task_7'}
    NUMBER = 5
    return redirect(url_for('square_res', number=NUMBER ** 2))


@app.route('/square/<int:number>')
def square_res(number: int):
    return str(number)


# Создать страницу, на которой будет форма для ввода имени и кнопка "Отправить"
# При нажатии на кнопку будет произведено перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
