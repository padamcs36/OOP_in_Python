class bio:
    def __init__(self):
        self.name =  "Padam"
        self.age = 22
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = bio() # cotain name that is Padam and age = 22
c1.age = 25 # updating the age to 25
c2 = bio() # cotain name that is Padam and age = 22
if c1.compare(c2): # now here c1 contian name=Padam and age=25 and c2 contain name that is Padam and age = 22
    print("They are same.")
else:
    print("They are not same.")