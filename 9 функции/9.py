
# def - обозачение начала функции 

def funk1(x, a):
    return x + a

def funk2(x):
    def add(a):
        return x + a
    return add
# передедовать, так и возвращать можно как списки, так и строки 
print(funk1(23, 12))

#в данном случае в переменную записыватеся первая функция funk2()
#следующим действием мы передаем еще одно значение в test(), но это мы уже работаем 
#с внутренней функцией и выводим оезультат 
test = funk2(100)
print(test(200))

# функции могут ничего не возвращать, чтобы это сделать, нало в конце ф-ии добавть словао pass, такакя 
# ф-я выведет None

def funk3():
    pass
print(funk3())

# в ф-ю можно передавать параметры по умолчанию 
def funk4(r, w, y = 2):
    res = r + w
    res *= y
    return res

print(funk4(2,4))

# в ф-ю можно передавать не ограниченное количество параметров, с помощью * 
# стоит учесть, что передается непосредственно кортеж, соответственно, его изменить нельзя
def funk5(*args):
    return args

print(funk5(2, 4, 5, 6))

#Чтобы передать словарь в качестве параметров, то нужно поставить **
def funk6(**args):
    return args

print(funk6(a=2, b=4, c=5, d=6))
print(funk6(short='dict', longer='dictionary'))

#анонимные функции, выводится в одну строку 
add = lambda x, y: x * y

print(add(34, 23))
#без создания переменной
print((lambda x, y: x * y)(45, 66))