class Computer:
    def __init__(self, ram, cpu):
        self.ram = ram
        self.cpu = cpu

    def get(self):
        print("Configuration is ", self.ram, self.cpu)

obj = Computer(16, "i5")
obj1 = Computer(8, "ADM")

obj.get()
obj1.get()