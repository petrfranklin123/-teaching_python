perem = 12
# print - это консольный вывод
print(perem)

#переменные нельзя начинать с цифр
#переменные res и Res абсолютно разные 
# input - это консольный ввод 

#num_1 = input("Enter first num ")
#num_2 = input("Enter second num ")
#print("Result ", num_1+num_2)

#В прошлом примере после введения чисел у нас получились строки 
#Чтобы в вводе получить целочисленное значние нужно добавить int, для дробного float и строки str
#эти функции можно применить к любому выводу, вводу или переменной 

num_1 = int(input("Enter first num "))
num_2 = int(input("Enter second num "))
print("Result 2 ", num_1+num_2)

#со строками работают арифметические операции типа + и *
res = 10
# чтобы удалить переменную нужно задействвать ф-ю del
del res