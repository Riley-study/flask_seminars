from flask import Flask, render_template

# Напишите простое веб-приложение на Flask, которое будет выводить на экран текст "Hello, World!".
# Добавьте две дополнительные страницы в ваше веб-приложение: страницу "about", страницу "contact".
# Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму.
# Написать функцию, которая будет принимать на вход строку и выводить на экран ее длину
# Написать функцию, которая будет выводить на экран HTML страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!".

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello world!"


@app.route('/about/')
def about():
    return "about"


@app.route('/contact/')
def contact():
    return "contact"


@app.route('/<int:num_1>/<int:num_2>')
def sum_num(num_1: int, num_2: int) -> str:
    return f'{num_1 + num_2}'


@app.route('/string/<string:text>/')
def length_text(text: str):
    return f'{len(text)}'

@app.route('/world/')
def world():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
