class Student:
    school_name="KaliSoft"
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    
    def getStudentInfo(self):
        print("Student Name ::",self.name)
        print("Student rollno ::", self.rollno)

    @classmethod
    def getSchoolInfo(cls):
        print("School Name ::", cls.school_name)
        
    @classmethod
    def getStudentSchholInfo(self, cls):
         print("Student Name ::",self.name)
         print("Student rollno ::", self.rollno)
         print("School Name ::", cls.school_name)

    
    @classmethod
    def m1(cls):
        print(id(cls))

s = Student("kali",101)

s.getStudentInfo()
s.getSchoolInfo()
s.m1()
s.getStudentSchholInfo()
print(id(Student))