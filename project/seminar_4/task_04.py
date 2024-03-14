# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и
# выводить результаты в консоль. � Используйте потоки.
import threading
import os

PATH = 'data'
count = 0


def get_amount_words(file_name: str) -> None:
    global count
    with open(file_name, encoding='utf-8') as f:
        count += len(f.read().split())
        print(f'промежуточное значение {count}')


if __name__ == '__main__':
    threads = []
    for root, dirs, files in os.walk(PATH):
        for file in files:
            file_path = os.path.join(root, file)
            thread = threading.Thread(target=get_amount_words, args=(file_path,))
            threads.append(thread)
            thread.start()
            print(f'{file}')

    for thread in threads:
        thread.join()

    print(f'Финальное значение счетчика: {count}')
