from datetime import datetime

from flask import Flask, render_template

# Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через контекст.

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello world!"


@app.route('/news/')
def news():
    news_list = [
        {'title': 'новость_1', 'description': 'Описание_1', 'date': datetime.now().strftime('%H:%M - %d.%m.%Y года')},
        {'title': 'новость_2', 'description': 'Описание_2', 'date': datetime.now().strftime('%H:%M - %d.%m.%Y года')},
        {'title': 'новость_3', 'description': 'Описание_3', 'date': datetime.now().strftime('%H:%M - %d.%m.%Y года')}]
    return render_template('news.html', news_list=news_list)






if __name__ == '__main__':
    app.run(debug=True)
