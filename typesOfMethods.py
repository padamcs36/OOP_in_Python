class Student:

    #class variable
    school = "Telusko"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    #Accessor (getter Method)
    def get_m1(self):
        return self.m1

    #Mutator(Setter Method)
    def set_m1(self, value):
        self.m1 = value

    #Now we are using class method for class method we are passing cls keyword
    #one Decorator that is @classmethod
    @classmethod
    def schoolName(cls):
        return cls.school

    #Now creating a static method by using @staticmethod decorator
    @staticmethod
    def info():
        print("I am admin of the school Telsuko...")

s1 = Student(33,21,75)
s2 = Student(89, 45, 23)

print(s1.avg())
print(s2.get_m1())
print(Student.schoolName())

s1.set_m1(99)
print(s1.get_m1())

Student.info()