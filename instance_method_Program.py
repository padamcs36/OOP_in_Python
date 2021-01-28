class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name: Mr: ", self.name)
        print("Marks Obtained: ", self.marks)
        self.grade()

    def grade(self):
        if self.marks <= 100 and self.marks >= 85:
            print("Grade is: A+")
        elif self.marks <= 84 and self.marks >= 75:
            print("Grade is: A")
        elif self.marks <= 74 and self.marks >= 65:
            print("Grade is: B+")
        elif self.marks <= 64 and self.marks >= 60:
            print("Grade is: B")
        elif self.marks <= 59 and self.marks >= 55:
            print("Grade is: C+")
        elif self.marks <= 54 and self.marks >= 50:
            print("Grade is: C")
        else:
            print("You are Failed.")
# name = input("Enter Student name: ")
# name = input("Enter Student name: ")
# obj = Student(name, mark)
# obj.display()
# # obj.grade()

#nth number of student.
std = int(input("Enter no: of  student: "))
for i in range(std):
    name = input("Enter Student name: ")
    mark = int(input("Enter Student mark: "))
    obj = Student(name, mark)
    obj.display()
    print("*"*20)