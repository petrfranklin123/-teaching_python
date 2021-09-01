import threading
import time 

# суммирует последовательность 
def hendler(started=0, finished=0):
    result = 0 
    for i in range(started, finished):
        result += i
    print('Value: ', result)


results = []
# разделяем интервал на два отрезка 
task1 = threading.Thread(
    target=hendler,
    #передаем от 2 до 12 
    kwargs={'finished': 2 ** 12}
)

task2 = threading.Thread(
    target=hendler,
    #передаем от 2 до 24
    kwargs={'started': 2 ** 12, 'finished': 2 **24}
)

started_at = time.time()

task1.start()
task2.start()

task1.join()
task2.join()

print('Result 1')
print('Time: {}'.format(time.time() - started_at))
print('Value: ', sum(results))

results = []
started_at = time.time()
hendler(finished= 2 ** 24)
print('Result 2')
print('Time: {}'.format(time.time() - started_at))
print('Value: ', sum(results))
