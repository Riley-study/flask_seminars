# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров. Например, создать страницы
# «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def home_page():
    return render_template('store.html')


@app.route('/bakery/')
def bakery():
    return render_template('bakery.html')

@app.route('/pies/')
def pies():
    return render_template('pies.html')


@app.route('/snacks_and_salads/')
def snacks_and_salads():
    return render_template('snacks_and_salads.html')


if __name__ == '__main__':
    app.run(debug=True)
