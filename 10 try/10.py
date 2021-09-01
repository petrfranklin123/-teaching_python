# обработка ошибок 
# деление на ноль
'''x = int(input())
y = int(input())

try: 
    res = x / y
# прописываем название ошибки 
except ZeroDivisionError:
    print("Вы ввели ноль")
    res = 0 
print(res)'''


'''try:
    x = int(input())
except ValueError:
    print("Вы ввели не число")
    x = 0
print(x)'''

# совмещенная программа
try:
    x = int(input())
except ValueError:
    print("Вы ввели не число")
    x = 0
# else выполняется в том случае, когда except не сработал 
else:
    print("вы ввели все верно")
# finally выполняется всегда, независимо от возникновения ошибок и исключений 
finally:
    print("Выполнится 100%")


try:
    y = int(input())
except ValueError:
    print("Вы ввели не число")
    y = 0


try: 
    res = x / y
# прописываем название ошибки 
except ZeroDivisionError:
    print("Вы ввели ноль")
    res = 0 
print(res)