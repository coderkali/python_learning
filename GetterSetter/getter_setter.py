class Employee:
    def __init__(self,name,salary):
        self.name= name
        self.salary=salary
    
    def set_name(self,name):
        new_name = name
        self.name= new_name

e = Employee("Kali", 1)
print(e.name)
e.name = "Prasad"
print(e.name)
e.set_name("Padhi")
print(e.name)