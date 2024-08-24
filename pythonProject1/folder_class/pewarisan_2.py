class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "gug-gug"
class Cat(Animal):
    def speak(self):
        return "meong"
def animal_sound(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(animal_sound(cat))
print(animal_sound(dog))

