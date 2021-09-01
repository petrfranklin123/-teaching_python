import requests
from time import time




def get_file(url):
    # учитывем редирект allow_redirects=True 
    r = requests.get(url, allow_redirects=True)
    return r

def write_file(response):
    #https://loremflickr.com/cache/resized/65535_51292800312_16b63e08ac_n_320_240_nofilter.jpg
    #достаем редиректнутую строку и сплитуем
    # забираем последний элемент массива  
    filename = response.url.split('/')[-1]
    # открываем файловый объект и сохраняем его в переменную file 
    with open(filename, 'wb') as file:
        # содержание данных ответа сервера в бинарном формате содержется в атрибуте content 
        file.write(response.content)

def main():
    t0 = time()
    url = "https://loremflickr.com/320/240"
    
    #10 раз будем повторять цикл 
    for  i in range(10):
        write_file(get_file(url))

    print(time() - t0)


#if __name__ == '__main__':
#    main()
#--------------- асинхронный уод

import asyncio

#для протокола HTTP используется
import aiohttp

#синхронная функция для записи ффайлов, так как asyncio не умеет работать асинхронно с файлами 
def write_image(data):
    #создаем название файла, куда записываем в шигурные скобки время записи
    filename = 'file-{}.jpeg'.format(int(time() * 1000))
    # запись данных 
    with open(filename, 'wb') as file:
        file.write(data)


async def fetch_content(url, session):
    # делаем асинхроный запрос по url с редиретком 
    async with session.get(url, allow_redirects=True) as response:
        #ждем загрузки БИНАРНЫХ ДАННЫХ read()
        data = await response.read()
        # вызываем синхронную функцияю записи изображений 
        # не рекомендуется, так как синхронные ф-ии в асинхронных потоках могут застопить всю программу 
        write_image(data)

async def main2():
    url = "https://loremflickr.com/320/240"

    tasks = []

    #открываем сессию 
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            # в данном блоке мы создаем новую задачу, по которой будет аперировать наша программа
            task = asyncio.create_task(fetch_content(url, session))
            # добавляем задачу в список задач 
            tasks.append(task)
        
        #дожидаемся работу задач прошлых 
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    t0 = time()
    #создаем асинхроный цикл 
    loop = asyncio.run(main2())
    #loop = asyncio.new_event_loop()
    #loop.run_until_complete(main2())
    #loop.close()
    print(time() - t0)