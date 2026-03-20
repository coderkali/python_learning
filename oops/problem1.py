class car:
    def __init__(self,make, model,year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print(f"The car is driving {self.model} of year {self.year} made by {self.make}")

c1 = car("Nissan","Sentra","2022")

c1.drive()