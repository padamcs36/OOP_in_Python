class car:
    wheels = 4 #class variable or static variable, once changed, then it is  change change for everyone.
    def __init__(self):
        self.mil = 10  # these are instance variable and changed for every object differently.
        self.com  = "BMW"

c1 = car()
c2 = car()

print(c1.com,c1.mil, car.wheels) #class variable can be invoked with the name of the class or object of the class.
c2.mil = 8 #instance variable only changed for c2 class object.
print(c2.com,c2.mil, c2.wheels)

print("Changing the class or static  variable.")
car.wheels = 5 # it is changed for both the object c1 and c2
print(c1.com,c1.mil, car.wheels)
print(c2.com,c2.mil, c2.wheels)