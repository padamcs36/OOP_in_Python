class Car:
    #a variable that is defined inside the class and outside the
    #init method is called class/static varaible
    wheels = 4

    def __init__(self): #variable defined inside it are called instance variable
        self.car = 'BMW'
        self.mil = 8


c1 = Car()
c2 = Car()

Car.wheels = 5 #now wheels value is updated for object c1 and c2

print(c1.car, c1.mil, Car.wheels)
print(c2.car, c2.mil, c2.wheels)