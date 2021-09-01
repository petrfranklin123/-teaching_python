#кортежи - это списки, которые нельзя изменить, можно только переприсвоить 
# обявление кортежа делается с помощью круглых скобок
# кортежи, в отличии от списков занимают меньше памяти 
a = ()
a = (43, 56, 66, 'str')
b = [33, 66, 55, 'seetr']

#функция определения выделенной памяти 
print(a.__sizeof__())
print(b.__sizeof__())

#функции для кортежей те же самые, что и для обычных списков