#try:
#   print(10 / 0)
#except ZeroDivisionError:
#    print("You can't divide by zero!")

try:
    numero = int(input("Enter a number: "))
    result = 10 / numero
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(f"The result is: {result}")