class Animal:
    __count = 0  # Статическая переменная-счётчик
    
    def __init__(self):
        Animal.__count += 1  # Увеличиваем счётчик при создании экземпляра
    
    def voice(self):
        pass
    
    @staticmethod
    def get_instances_count():
        return Animal.__count

# Классы-наследники (без изменений)
class Dog(Animal):
    def voice(self):
        return "Гав!"

class Cat(Animal):
    def voice(self):
        return "Мяу!"

class Cow(Animal):
    def voice(self):
        return "Мууу!"

# Создание экземпляров
dog = Dog()
cat = Cat()
cow = Cow()

# Вызов методов voice()
print(dog.voice())  # Вывод: Гав!
print(cat.voice())  # Вывод: Мяу!
print(cow.voice())  # Вывод: Мууу!

# Вывод количества созданных экземпляров
print("Количество экземпляров:", Animal.get_instances_count())  # Вывод: 3
