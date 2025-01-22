name = input("What is your name")
print("hello", name)
age = input("how old are you? ")
try:
    age = int(age)  # i'm trying to convert it to a number
    print("you were probably born in", 2024 - int(age))

except ValueError:
    print("you are trying to trick me")
    print('better luck next time')

except ZeroDivisionError:
    print('you cant divide by 0')

except:
    print('something unexpected happened')
else: # this happens if no error ocurred
    print("you were probably born in", 2024 - age)

finally:
    print("thanks for playing")