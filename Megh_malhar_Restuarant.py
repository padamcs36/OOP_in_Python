import sys
class hotel:
    hotel_name = "MEGHMALAHR"
    def __init__(self, name):
        self.name = name

    def for_tea(self, half=0, full=0):
        tea_result = half * 25 + full * 50
        print("Sir Your Bill is: ", tea_result)

    def vegeterain(self, beryani=0, dal_mass=0, dal_chawal=0, meals=0, bindi=0):
        vege_bill = beryani * 70 + dal_mass * 80 + dal_chawal * 50 + meals * 10 + bindi * 70
        print("Sir You Bill is: ", vege_bill)

    def non_vege(self,beryani=0, dal_mass=0, dal_chawal=0, meals=0, bindi=0, chicken=0, chicken_fry=0, mutton=0, tika=0):
        non_vege_bill = beryani * 70 + dal_mass * 80 + dal_chawal * 50 + meals * 10 + bindi * 70 + chicken * 800 + chicken_fry * 900 + mutton*1200+tika*180
        print("Sir Your Bill is: ", non_vege_bill)

print("Welcome to ", hotel.hotel_name, " Restuarant")
name = input("Enter Your name for entry: ")

obj = hotel(name)

while True:
    option = input("t-for tea\nv-Vegeterain\nn-Non-Vegeterain\ne-Exit: ")
    if option.lower() == 't':
        print("Menu for Tea")
        print("Half cup is: 25\nFull Cup is: 50")
        half = int(input("Enter half cup tea in digits: "))
        full = int(input("Enter full cup tea in digits: "))
        obj.for_tea(half, full)
    elif option.lower() == 'v':
        print("Menu  for Vegetrain")
        print("Beryani fee plate is: 70\nDal-mass fee plate is: 80\ndal_chawal fee plate: 50\nBindi fee plate is: 70\nMeal fee price is: 10")
        beryani = int(input("Enter number of plate for beryani: "))
        dal_mass = int(input("Enter number  of plate for dal_mass: "))
        dal_chawal = int(input("Enter number of plate for dal_chawal: "))
        meals = int(input("Enter number of meals: "))
        bindi = int(input("Enter number of plate for bindi: "))
        obj.vegeterain(beryani, dal_mass, dal_chawal, meals, bindi)

    elif option.lower() == 'n':
        print("Beryan fee plate is: 70\nDal-mass fee plate is: 80\ndal_chawal fee plate: 50\nBindi fee plate is: 70")
        print("Chicken fee Kilo is: 800\nChicken-fry fee kilo is: 900\nMutton fee kilo is: 1200")
        beryani = int(input("Enter number of plate for beryani: "))
        dal_mass = int(input("Enter number  of plate for dal_mass: "))
        dal_chawal = int(input("Enter number of plate for dal_chawal: "))
        meals = int(input("Enter number of meals: "))
        bindi = int(input("Enter number of plate for bindi: "))
        chicken = float(input("Enter chicken in kg: 0.5 or 1kg: "))
        chicken_fry = float(input("Enter chicken_fry in kg: "))
        mutton = float(input("Enter mutton in kg: "))
        tika = int(input("Enter tika in number of peices: "))
        obj.non_vege(dal_mass,dal_chawal,mutton,meals,chicken,chicken_fry,tika,beryani, bindi)
    else:
        print("Thank You for Visiting our restaurant")
        sys.exit()









