import threading
import time 

def producer():
    time.sleep(10)
    print('Product found!')
    # отправляет данные (пропуск) wait(), пока set() не будет вызвано, wait() будет в заблокированном состоянии 
    product.set()
    # очистка событий, wait() будет заблокировано 
    product.clear()

def consumer():
    print("Product wait")
    product.wait()
    print("Product exists!")

# создаем экземпляр события 
product = threading.Event()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=consumer)

task1.start()
task2.start()

task1.join()
task2.join()