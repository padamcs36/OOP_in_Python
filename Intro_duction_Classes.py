class computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Configuration is: ", self.cpu, self.ram)

obj  = computer("i7", 16)
obj1 = computer("m3", 8)

obj.config()
obj1.config()

# ob = computer()
# cpu = input("Enter CPU: ")
# ram = int(input("Enter RAM you need: "))
# ob.config(cpu, ram)
