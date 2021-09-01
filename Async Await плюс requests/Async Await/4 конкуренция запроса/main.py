import time
import random
import asyncio
import aiohttp

URL = 'https://api.github.com/events'
MAX_CLIENTS = 3


async def fetch_async(pid):
    start = time.time()
    sleepy_time = random.randint(2, 5)
    print('Fetch async process {} started, sleeping for {} seconds'.format(
        pid, sleepy_time))

    await asyncio.sleep(sleepy_time)

    async with aiohttp.request('GET', URL) as response:
        datetime = response.headers.get('Date')

    response.close()
    return 'Process {}: {}, took: {:.2f} seconds'.format(
        pid, datetime, time.time() - start)


async def asynchronous():
    start = time.time()
    futures = [fetch_async(i) for i in range(1, MAX_CLIENTS + 1)]
    for i, future in enumerate(asyncio.as_completed(futures)):
        result = await future
        print('{} {}'.format(">>" * (i + 1), result))

    print("Process took: {:.2f} seconds".format(time.time() - start))


ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()

'''
Fetch async process 3 started, sleeping for 5 seconds
Fetch async process 2 started, sleeping for 2 seconds
Fetch async process 1 started, sleeping for 3 seconds
>> Process 2: Sun, 11 Jul 2021 06:19:22 GMT, took: 2.62 seconds
>>>> Process 1: Sun, 11 Jul 2021 06:19:22 GMT, took: 3.28 seconds
>>>>>> Process 3: Sun, 11 Jul 2021 06:19:22 GMT, took: 5.28 seconds
Process took: 5.28 seconds
'''