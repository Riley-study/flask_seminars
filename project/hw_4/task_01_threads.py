# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое
# изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени
# выполнения программы.
import os
import threading
import requests
import time

urls = [
    'https://i.pinimg.com/736x/be/39/7c/be397c91b8026b17f5f8a6ed98e23e9e.jpg'
    'https://media.contented.ru/wp-content/uploads/2022/12/3-1024x681.png',
    'https://upload.wikimedia.org/wikipedia/commons/c/c9/Moon.jpg',
    'https://www.img2go.com/assets/dist/sample-files/img/convert_to_jpg.png',
    'https://cs6.livemaster.ru/storage/c1/ad/0fb10c243c18873254c4ac194epd.jpg',
    'https://habrastorage.org/r/w1560/webt/xh/7m/8n/xh7m8nokzhgfqixb00fnwcmkthm.jpeg',
    'https://dkrotov.com/delight.webpconverter/webp_converter_test_image.jpg'
]


def download_picture(url_picture):
    response = requests.get(url_picture)
    if response.status_code == 200:
        image_name = url_picture.split('/')[-1]
        image_path = os.path.join('images', image_name)
        with open(image_path, 'wb') as file:
            file.write(response.content)
        print(f'Image downloaded successfully and saved as {image_name}')
    print(f"Downloaded {url_picture} in {time.time() - start_time:.2f} seconds")


threads = []
start_time = time.time()
for url in urls:
    thread = threading.Thread(target=download_picture, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
