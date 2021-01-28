class Student:
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setMark(self, mark):
        self.mark = mark
    def getMaark(self):
        return self.mark
    # def getGrade(mark):
    #     if mark <= 100 and mark >= 85:
    #         print("Grade is: A+")
    #     elif mark <= 84 and mark >= 75:
    #         print("Grade is: A")
    #     elif mark <= 74 and mark >= 65:
    #         print("Grade is: B+")
    #     elif mark <= 64 and mark >= 60:
    #         print("Grade is: B")
    #     elif mark <= 59 and mark >= 55:
    #         print("Grade is: C+")
    #     elif mark <= 54 and mark >= 50:
    #         print("Grade is: C")
    #     else:
    #         print("You are Failed.")
std = int(input("Enter number of student."))
for i in range(std):
    name = input("Enter name of the student: ")
    mark = int(input("Enter mark of the student: "))
    s = Student()
    s.setName(name)
    s.setMark(mark)
    print("Name of student is: ", s.getName())
    print("Marks obtained is: ", s.getMaark())
    print("*"*25)