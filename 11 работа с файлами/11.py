f = open("text.txt", "r")


#функция read читает весь файл, в качестве параметра можно добавть индекс элемента, которого нужо прочесть
print(f.read())

for line in f:
    print(line)

#нужно всегда закрывать файл
f.close()

z = open("text.txt", "w")

z.write("Hi, it\'s me! \nTest")
z.close()