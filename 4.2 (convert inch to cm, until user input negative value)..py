#Write a program that converts inches to centimeters
# until the user inputs a negative value. Then the program ends.

value = float(input("Enter your length in inches, enter negative (-) to exit: "))
while value >= 0 :
    cm = value * 2.54
    print(f"{value} inches is {cm} centimeter")
    value = float(input("Enter your length in inches, enter negative (-) to exit: "))

