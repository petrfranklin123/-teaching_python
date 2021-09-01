#num = input("Введите ваше имя")

#if num == 'test':
#    print("true name\n")

'''num = int(input("Введите число "))

if num == 12:
    print("number 12\n")
elif num < 0:
    print("number < 0\n")
elif num > 0:
    print("number > 0\n")
else:
    print("число не определено")

#сокращенная запись условного оператора 
name = input("Введите слово")
#если срабатывает условие if то присваивается "Yes" иначе "No"
A = "Yes" if name != "Test" else "No"
print(A)'''

'''a = int(input())
b = int(input())
c = int(input())

if b <= a and b >= c:
    print('\n',a,'\n',b,'\n',c)

elif a <= b and a >= c:
    print('\n',b,'\n',a,'\n',c)

elif b <= c and c >= a:
    print('\n',c,'\n',b,'\n',a)

elif c <= a and c >= b:
    print('\n',a,'\n',c,'\n',b)

elif c <= b and c >= a:
    print('\n',b,'\n',c,'\n',a)

elif a <= c and a >= b:
    print('\n',c,'\n',a,'\n',b)'''

'''if 'a' >= 'b' >= 'c':
    print(a,'\n',b,'\n',c)
elif 'b' >= 'a' >= 'c':
    print(b,'\n',a,'\n',c)
elif 'c' >= 'b' >= 'a':
    print(c,'\n',b,'\n',a)
elif 'a'>= 'c' >= 'b':
    print(a,'\n',c,'\n',b)
elif 'b'>= 'c' >= 'a':
    print(b,'\n',c,'\n',a)
elif 'c' >= 'a'>= 'b':
    print(c,'\n',a,'\n',b)'''


'''a = int(input())
b = int(input())
c = int(input())

accum = 0 
accum = a
if a < b:
    accum = b
    if b < c:
        accum = c 
elif a < c:
    accum = c

print(accum)'''

string = input()

str1 = eval(string[0]+string[1]+string[2])
str2 = eval(string[3]+string[4]+string[5])

if str1 == str2:
    print("Удачливый сукин сын")
else:
    print("Ты еблан")