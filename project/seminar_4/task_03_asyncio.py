# Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого адреса.
# � После загрузки данных нужно записать их в отдельные файлы.
# � Используйте асинхронный подход

import asyncio
import aiohttp
import time

urls = [
    'https://translate.google.com/',
    'https://www.youtube.com/',
    'https://paiza.io/',
    'https://mail.google.com/',
    'https://google.com/',
    'https://ya.ru/',
    'https://mail.ru/',
    'https://jsonformatter.org/',
    'https://img2txt.com/ru'
]


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = 'data/asyncio_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
            with open(filename, "w", encoding='utf-8') as f:
                f.write(text)
                print(f"Downloaded {url} in {time.time() - start_time: .2f} seconds")


async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

start_time = time.time()

if __name__ == '__main__':
    asyncio.run(main())
