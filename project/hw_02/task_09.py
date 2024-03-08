# Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке
# будет создан cookie-файл с данными пользователя, а также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя. На странице приветствия должна быть кнопка «Выйти»,
# при нажатии на которую будет удалён cookie-файл с данными пользователя и произведено перенаправление
# на страницу ввода имени и электронной почты.

from flask import Flask, render_template, request, abort, redirect, url_for, flash, make_response, session


app = Flask(__name__, template_folder='templates')

app.secret_key = b'1a214ca8bf50c2ae4784b444f23412ae0d5d8c16ae98128e3d549546221265e84'


@app.route('/')
def index():
    return render_template('authorization.html')


@app.route('/authorization/', methods=['GET', 'POST'])
def authorization():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        response = make_response(redirect('/hello_page/'))
        response.set_cookie('user_data', f'{name}:{email}')
        return response



@app.route('/hello_page/', methods=['GET', 'POST'])
def hello_page():
    user_data = request.cookies.get('user_data')
    if user_data:
        name, _ = user_data.split(':')
        return render_template('hello_page.html', name=name)
    else:
        return redirect('/')


@app.route('/logout/')
def logout():
    response = make_response(redirect('/'))
    response.set_cookie('user_data', '', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
