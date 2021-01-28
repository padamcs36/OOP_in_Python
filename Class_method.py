class Animal:
    legs = 4 #static variable, acces with the name  of the class. it is common for all the objects.
    @classmethod
    def walk(cls, name): #name is local variable.
        print("{} walks with {} legs.".format(name, cls.legs)) #Animal.legs but we are inside the method, we have cls variable.

Animal.walk("Dog")
Animal.walk("Cat")



#without any decorator then this method is either instance or static method.
class Test:
    count = 0
    def __init__(self):
        Test.count = Test.count + 1 #Static variable

    @classmethod #whenever we are creating class method then @classmethod decorator is defined before the method.(compulsory)
    def getNoOfObjects(cls):
        print("The number of objects created is: ", Test.count)

    @staticmethod #decorator
    def sum(x, y):
        print("The sum is: ", x+y)

t1 = Test()
t2 = Test()
# t3 = Test()
Test.getNoOfObjects()
Test.sum(4, 6)