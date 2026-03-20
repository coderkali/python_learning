class Employee:
    def __init__(self,salary,name,location,company):
        self.salary = salary
        self.name = name
        self.location = location
        self.company = company

    def get_salary(self):
        print(f"The salary for {self.name} working in {self.company} is {self.salary}")
    
    def get_location(self):
        print(f"The location of the company {self.company} is {self.location}")


e1 = Employee(100000,"Kali","California","Google")
e1.get_salary()
e1.get_location()