import threading
import time 

print(threading.active_count())
current = threading.current_thread()
print(current.getName())
print(current.is_alive())

#то что произойдет, ели мы попросбуем запкстить еще раз 
try:
    current.start()
except RuntimeError as e:
    print("ERROR: {error}".format(error=e))
current.setName('SuperThread')
print(current.getName())

#getName  и setName - это устаревший интерфейс, в реальных задачах используют напрямую атрибут name 
current.name = "SuperThread1"
print(current.name)
print(current.getName())

#вывод всех запущенных и живых тредов 
print(threading.enumerate())

# пример для демонстации потокобезопасного хранилища данных 
thread_data = threading.local()
thread_data.value = 5


def print_result():
    print(threading.current_thread())
    print("Result: {}".format(thread_data.value))

def counter(started, to_value):
    print(hasattr(thread_data, "value"))
    thread_data.value = started
    for i in range(to_value):
        thread_data.value += 1
    print_result()

#args - передаем данные 
task1 = threading.Thread(target=counter, args=(0, 10), name="Task1")
task2 = threading.Thread(target=counter, args=(100, 3), name="Task2")

task1.name = "task1"
task2.name = "task2"

task1.start()
task2.start()

task1.join()
task2.join()

print(print_result())