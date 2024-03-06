# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров. Например, создать страницы
# «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('store.html')


@app.route('/bakery/')
def about():
    return render_template('bakery.html')


@app.route('/meat_pies/')
def about():
    return render_template('meat_pies')


@app.route('/Snacks_and_salads/')
def about():
    return render_template('Snacks_and_salads')

if __name__ == '__main__':
    app.run()
