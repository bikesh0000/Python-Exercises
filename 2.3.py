#Write a program that asks the user for the length and width of a rectangle.
# The program then prints out the perimeter and area of the rectangle.
# The perimeter of a rectangle is the sum of the lengths of each four sides.

length = int(input("Enter your length here: "))
width = int(input("Enter your width here: "))
Area_of_the_rectangle = length * width
print(f"The area of the rectangle is {Area_of_the_rectangle}")
Perimeter_of_the_rectangle = 2 * (length + width)
print(f"The perimeter of the rectangle is {Perimeter_of_the_rectangle}")