from random import choices
from random import choices

drinks = ("gin", "vodka", "tequila", "sake")
name = input("I'm the virtual bartender. What is your name? ")
try:
    age = input("What is your age? ")
    age = int(age)

    country = input("What is your country? ")

    legal = False
    if age >= 21:
        legal = True
    elif age >= 18 and (country != "USA" and country != "UAE"):
        legal = True
    elif age >= 16 and country == "Luxembourg":
        legal = True

except ValueError:
    print("Don't play games with me!")

else:
    if legal:
        print("dear", name, "its a pleasure to serve you", choices(drinks))
    else:
        print("dear", name, "unfortunately i cant serve you")

