class Animal:
    def voice(self):
        pass

# 1. Создаем три класса-наследника
class Dog(Animal):
    def voice(self):
        return "Гав!"

class Cat(Animal):
    def voice(self):
        return "Мяу!"

class Cow(Animal):
    def voice(self):
        return "Мууу!"

# 2. Создаем экземпляры и вызываем метод voice()
dog = Dog()
cat = Cat()
cow = Cow()

print(dog.voice())  # Вывод: Гав!
print(cat.voice())  # Вывод: Мяу!
print(cow.voice())  # Вывод: Мууу!
