class Person: 
    def __init__(self,name,age):
        self.name= name
        self.age=age
    
p1 = Person("Kali","35")

print(p1.name)
print(p1.age)


class Animal:
    def sound(self):
        print("Animal is makig a sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog is makinga sound")

dog = Dog();
dog.sound()
