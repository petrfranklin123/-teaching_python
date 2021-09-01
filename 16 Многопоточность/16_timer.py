import os
import threading


def exec_watcher():
    # отсчет в пять секунд до запуска функции print_files
    timer = threading.Timer(5.0, print_files)
    timer.start()

# выводит все фалы в дериктории 
def print_files():
    for i in os.listdir('.'):
        print(i)
    exec_watcher()

exec_watcher()