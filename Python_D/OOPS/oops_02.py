class TestStudent:
    def __init__(self):
        self.name = "Kali"
        self.marks = 80
    
    def talk(self):
        print("Hello My Name is ", self.name)
        print("Hello My Name is ", self.marks)

s = TestStudent()
print(s.name)
print(s.marks)
s.talk()