class Student:

    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    
    def talk(self):
        print("Hello My Name is ", self.name)
        print("Hello My Marks are ", self.marks)
        print("Hello My rollno is ", self.rollno)

s1 = Student("Kali",101,90)
s1.talk()