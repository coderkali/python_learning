class Employee:
    company = "Google"
    salary = 100000
    location = "California"


    def get_salary(self, name):   
        print(f"The salary for {name} working in {self.company} is {self.salary}")

    def get_location(self):
        print(f"The location of the company {self.company} is {self.location}")

    def empleyee_info(self, name):
        self.get_salary(name)
        self.get_location()


e= Employee()
e.get_salary("Kali")
e.get_location()
e.empleyee_info("Kali")