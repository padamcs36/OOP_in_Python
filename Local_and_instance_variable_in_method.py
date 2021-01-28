class Test:
    def average(self, list):
        a = 30 #this is local variable, it can be call inside the method
        result = sum(list)/len(list)
        print("The average is: ",result)
        print("Local Variable a: ",a)

t = Test()
t.average([10,20,30,40,50])
# print(a) #NameError: name 'a' is not defined because it is defined inside the method.
#list as argument is a instance variable.