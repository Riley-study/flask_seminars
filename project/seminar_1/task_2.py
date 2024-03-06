# Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через контекст.

from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello world!"


@app.route('/students/')
def students():
    head = {
        'name': 'Имя',
        'surname': 'Фамилия',
        'age': 'Возраст',
        'rate': 'Средний балл'
    }

    students_list = [{'name': 'Иван', 'surname': 'Иванов', 'age': 25, 'rate': 4.5},
                     {'name': 'Екатерина', 'surname': 'Сомина', 'age': 20, 'rate': 5.0},
                     {'name': 'Александр', 'surname': 'Петров', 'age': 18, 'rate': 3.0}]
    return render_template('index.html', **head, students_list=students_list)


if __name__ == '__main__':
    app.run(debug=True)
