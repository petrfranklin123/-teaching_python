# множества расположение элементов происходит в случаном порядке 

a = set ()

# функция type() возвращает тип данных 

print(type(a))
print(a)

# множества могут объявляться без set, а с {}
# но в отличии от словарей, там прописываются просто данные, без ключей 

a = {'23', 34}


# frozenset в этом случае у нас тоже множество, но его видоизменять нельзя 

b = frozenset("QWERTY")

# пример множества 
a = ['r', 's', 'w', 'a', 's', 'w']

print(a)
# таким образом мы отсекаем все повторения в списке
print(set(a))

#функции с множествами 

a = {32, 45, 43.23, 76}

# вывод количества элементов 
print(len(a))

# проверка принадлежности множеству переменной 
x = 45
print(x in a)

#проверка на схожесть 
a = {32, 45, 43.23, 76}
x = {67, 45, 90}
print(a == b)

# объединение множеств 
a.update(x)
print(a)

#нахождение пересечения 
a = {32, 45, 43.23, 76}
x = {67, 45, 90}
a.intersection_update(x)
print(a)

#вывод отличных элементов 
a = {32, 45, 43.23, 76}
x = {67, 45, 90}
a.symmetric_difference_update(x)
print(a)

#добавление элемента в множество 
a = {32, 45, 43.23, 76}
a.add(46)
print(a)

#удаление элемента, если не находит элемента, то выдает ошибку 
a = {32, 45, 43.23, 76}
a.remove(32)
print(a)

#удаление элемента без ошибки 
a = {32, 45, 43.23, 76}
a.discard(32)
print(a)

#очищение 
a.clear()