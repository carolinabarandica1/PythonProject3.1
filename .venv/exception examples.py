name = input("What is your name")
print("hello", name)
age = input("how old are you? ")
try:
    age = int(age)  # i'm trying to convert it to a number
    print("you were probably born in", 2024 - int(age))

except:
    print("you are trying to trick me")