l = [34, 'sd', 56, 66.666]
# В питоне можно сделать отрицательный индек, это значит, что будет выбираться элементы с конца
print("Это последний элемент: ", l[-1])
#вывод списка
i = 0 

while i < 4:
    print(l[i])
    i += 1

#Существует подобная конструкция, которая служит для вывода списка 
# где START это индекс начала вывода
# STOP индекс окончания 
# STEP шаг вывода
# l[START:STOP:STEP]

#пордобная запись прсото выведет массив стандартно
print(l[:])

#в срезах можно писать отрицательные индексы
#так же в этих срезах можно реализовывать не законченные записи типа 
# l[-2::-2]
# l[::2]