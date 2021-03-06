# словария, это ассоциативные массивы 
# 1 метод 
d = {}
print(d)

d = {'test' : 1, 'test_2' : "Test"}

print(d['test'])
print(d['test_2'])

# 2 матод

f = dict (short =  "dict", longer = "dictionary")
#переприсваивание значения 
f['short'] = 234
print(f)

# 3 метод 

g = dict([[23, 34],[56, 78]])

print(g)

# 4 метод

# в этом примере всем именам присваевается единица 
h = dict.fromkeys(['a', 'b', 'c'], 1)

# 5 метод

# в этом примере словарь заполняется с помощью цикла 
# ключ от 0 до 6, а значение в квадрате присваевается ключу, с помощью ф-ии range, которая повторяет действие 
# в нашем случае 7 раз 
q = {a : a**2 for a in range(7)}
print(q)

person = {'name' : {'last_name': 'Иванов', 'first_name': 'Иван', 'middle_name': 'Иванович'}, 'address': ['г. Андрюшки', 'ул. Васильковская д. 23б', 'кв.12'], 'phone': {'home_phone': '34-67-12', 'mobile_phone': '8-564-345-23-65', 'mobile_phone_2': 'Нет'}}

print(person["name"]["last_name"])

print(person["address"][0])

# функции со словарями 

qwer = {}
# Очищает словарь 
qwer.clear()
# возвращает копию ловаря 
qwer.copy()
# возвращает значение ключа, если его нет, возвращает default 
qwer.get(key [, default])
# возвращает ключ и значени 
qwer.items()
# возвращает ключи в словаре 
qwer.keys()
#  удаляет ключ и возвращает значени 
qwer.pop(key [, default])
# удаляет и возврщает пару ключ и значение
qwer.popitem()
# обновляет словарь, добавляя в него ключи и значения 
qwer.update([other])
# возвращает значения в словаре 
qwer.values()