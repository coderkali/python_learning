class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    def make_sound(self):
        super().make_sound()
        print("Woof!")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    def make_sound(self):
        print("Meow!")

dog = Dog("Tommy", "Labrador")
print(dog.name)
print(dog.species)
print(dog.breed)
dog.make_sound()
