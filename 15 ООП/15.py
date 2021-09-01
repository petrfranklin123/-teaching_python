class Person:
    name = "Ivan"
    age = 10 
# в классах функции называются Методами, а переменные называются полями 
# во всех методах должен присутствовать аргумент self 
    def set(self, name, age):
        # с помощью self мы обращаемся к классу и берем от туда переменные 
        self.name = name
        self.age = age
        # данная функция присваивает пересланные данные к классу


# создаем объекты 

vlad = Person()
'''
#переприсваиваем 
vlad.name = "Влад"
print(vlad.name)
'''
# вызываем классовую функцию
vlad.set("Влад", 25)
print(vlad.name, " ", vlad.age)

ivan = Person()
#переприсваиваем 
ivan.age = 45
print(ivan.name)