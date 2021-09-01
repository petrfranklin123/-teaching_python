import threading
import time 

def producer():
    print('Set locking')
    #захватываем блокировку, печатаем данные 
    with lock:
        print('done')
        # ожидаем освобождения блокировки, но она никогда не освободится 
        with lock:
            print("It's great")
    print("Locking release!")

# создаем экземпляр  
lock = threading.Lock()
'''# захват блокировки для выполнения кода 
lock.acquire()
print(1)
print(1)
print(1)
# отдаем блокировку другому потоку 
lock.release()'''


task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)
#два потока потока попытаются захватить блокировку и лишь один сможет это сделать 
#другой же не получит блокировку и будет бесконечно ожидать 
task1.start()
task2.start()

task1.join()
task2.join()