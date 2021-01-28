import sys
class bank:
    bankname = 'UBL'
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
    def see_amount(self):
        print("Your current Balance is: ", self.balance)
    def deposit(self,amt):
        self.balance = self.balance+amt
        print("After Deposite your amount is: ", self.balance)

    def withdraw(self, amt):
        if amt>self.balance:
            print("Insufficient Fund, cannot perform this operation.")
            sys.exit()
        self.balance = self.balance - amt
        print("After withraw your amount is: ", self.balance)


print("Welcome to ", bank.bankname)
name = input("Enter your name: ")
obj = bank(name)
count = 0
while True:
    print("s-see amount\nd-deposit\nw-withdraw\ne-exit")
    option = input("Enter your choice: ")

    if option == 'd' or option == 'D':  # if option.lower() == 'd':
        amt = float(input("Enter amount to deposit: "))
        obj.deposit(amt)
        count = 0
    elif option == 'w' or option == 'W':
        amt = float(input("Enter amount to withdraw: "))
        obj.withdraw(amt)
        count = 0
    elif option == 'e' or option == 'E':
        print("Thanks for using UBL Bank")
        sys.exit()
    elif option.lower() == 's':
        obj.see_amount()
    else:
        print("Choose valid option.")
        count += 1
        if(count > 3):
            print("You entered many times wrong option continously so further cannot perform operation.")
            sys.exit()
