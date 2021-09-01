import threading
import time 

# суммирует последовательность 
def hendler(started=0, finished=0):
    result = 0 
    for i in range(started, finished):
        result += i
    print('Value: ', result)

params = {'finished': 2 ** 26}

# создаем экземпляр класса треда 
# target= указываем, что именно будет запущено в треде 
# kwargs= передваваемые параметры 
task = threading.Thread(target=hendler, kwargs=params)
started_at = time.time()
print('Result 1')
# подготавливаем тред и запускаем
task.start()
# блокируем интерпритатор до того момента, пока функция не отработает 
task.join()
print('Time: {}'.format(time.time() - started_at))

started_at = time.time()
print('Result 2')
hendler(**params)
print('Time: {}'.format(time.time() - started_at))