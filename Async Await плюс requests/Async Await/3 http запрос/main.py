import time
import urllib.request
import asyncio
import aiohttp

URL = 'https://api.github.com/events'
MAX_CLIENTS = 3


def fetch_sync(pid):
    print('Fetch sync process {} started'.format(pid))
    start = time.time()
    response = urllib.request.urlopen(URL)
    datetime = response.getheader('Date')

    print('Process {}: {}, took: {:.2f} seconds'.format(
        pid, datetime, time.time() - start))

    return datetime


async def fetch_async(pid):
    print('Fetch async process {} started'.format(pid))
    start = time.time()
    async with aiohttp.request('GET', URL) as response:
        datetime = response.headers.get('Date')

    print('Process {}: {}, took: {:.2f} seconds'.format(
        pid, datetime, time.time() - start))

    response.close()
    return datetime


def synchronous():
    start = time.time()
    for i in range(1, MAX_CLIENTS + 1):
        fetch_sync(i)
    print("Process took: {:.2f} seconds".format(time.time() - start))


async def asynchronous():
    start = time.time()
    tasks = [asyncio.ensure_future(
        fetch_async(i)) for i in range(1, MAX_CLIENTS + 1)]
    await asyncio.wait(tasks)
    print("Process took: {:.2f} seconds".format(time.time() - start))


print('Synchronous:')
synchronous()

print('Asynchronous:')
ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()

'''
Synchronous:
Fetch sync process 1 started
Process 1: Sun, 11 Jul 2021 05:44:15 GMT, took: 0.68 seconds
Fetch sync process 2 started
Process 2: Sun, 11 Jul 2021 05:44:15 GMT, took: 0.31 seconds
Fetch sync process 3 started
Process 3: Sun, 11 Jul 2021 05:44:15 GMT, took: 0.29 seconds
Process took: 1.28 seconds
Asynchronous:
Fetch async process 1 started
Fetch async process 2 started
Fetch async process 3 started
Process 1: Sun, 11 Jul 2021 05:43:57 GMT, took: 0.34 seconds
Process 3: Sun, 11 Jul 2021 05:43:57 GMT, took: 0.32 seconds
Process 2: Sun, 11 Jul 2021 05:43:57 GMT, took: 0.33 seconds
Process took: 0.36 seconds
'''