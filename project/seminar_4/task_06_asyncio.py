# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и
# выводить результаты в консоль. � Используйте асинхронный подход.

import asyncio
from pathlib import Path
import os

PATH = 'data'
count = 0


async def get_amount_words(file_name: str) -> None:
    global count
    with open(file_name, encoding='utf-8') as f:
        count += len(f.read().split())
        print(f'промежуточное значение {count}')

async def main():
    tasks = []
    for root, dirs, files in os.walk(PATH):
        for file in files:
            file_path = os.path.join(root, file)
            tasks.append(asyncio.create_task(get_amount_words(file_path)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
    print(f'Финальное значение счетчика: {count}')