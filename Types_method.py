class Student:
    def __int__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3



# ob = Student(90,77,84)
# print(ob.m1, ob.m2, ob.m3)