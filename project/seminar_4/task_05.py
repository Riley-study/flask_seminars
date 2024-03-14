# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и
# выводить результаты в консоль. � Используйте процессы.
import multiprocessing
import os

PATH = 'data'
count = multiprocessing.Value('i', 0)


def get_amount_words(file_name: str, counter) -> None:
    with open(file_name, encoding='utf-8') as f:
        with counter.get_lock():
            counter.value += len(f.read().split())
    print(f'промежуточное значение {counter.value}')


if __name__ == '__main__':
    processes = []
    for root, dirs, files in os.walk(PATH):
        for file in files:
            file_path = os.path.join(root, file)
            process = multiprocessing.Process(target=get_amount_words, args=(file_path, count))
            processes.append(process)
            process.start()
            print(f'{file}')

    for process in processes:
        process.join()

    print(f'Финальное значение счетчика: {count.value}')
