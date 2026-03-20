class Employee:
    company = "Tesla"

    def __init__(self, salary, name, location):
        self.salary = salary
        self.name = name
        self.location = location
        #self.company = company

    def get_salary(self):
        print(f"The salary for {self.name} working in {self.company} is {self.salary}") 

    def get_location(self):
        print(f"The location of the company {self.company} is {self.location}") 

e1 = Employee(100000, "Kali", "California")
e1.get_salary()
e1.get_location()
print(Employee.company) # Output: Tesla
print(e1.company) # Output: Tesla
print(dir(e1))