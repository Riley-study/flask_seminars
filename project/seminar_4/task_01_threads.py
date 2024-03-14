# Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого адреса.
# � После загрузки данных нужно записать их в отдельные файлы.
# � Используйте потоки.
import threading
import requests
import time

urls = [
    'https://translate.google.com/',
    'https://vk.com/',
    'https://www.youtube.com/',
    'https://paiza.io/',
    'https://mail.google.com/',
    'https://google.com/',
    'https://ya.ru/',
    'https://mail.ru/',
    'https://jsonformatter.org/',
    'https://img2txt.com/ru'
]




def download(url):
    response = requests.get(url)
    filename = 'threading_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")

threads = []
start_time = time.time()
for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
