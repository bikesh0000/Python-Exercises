#Write a program that asks the user for three integer numbers.
# The program prints out the sum, product, and average of the numbers.

a = int(input("Enter the first integer number here: "))
b = int(input("Enter the second integer number here: "))
c = int(input("Enter the third integer number here: "))

sum = (a + b + c)
product = (a * b * c)
average = ((a + b + c) / 3)
print(f"The sum of the three integer numbers are {sum}")
print(f"The product of the three integer numbers are {product}")
print(f"The average of the three integer numbers are {average}")