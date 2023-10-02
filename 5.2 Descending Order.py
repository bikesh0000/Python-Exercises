#Write a program that asks the user to enter numbers until they input an empty string to quit.
# #At the end, the program prints out the five greatest numbers sorted in descending order.
#Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.

numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break

    number = float(user_input)
    numbers.append(number)

if len(numbers) < 5:
    print("Enter at least 5 numbers to display the five greatest numbers.")
else:
    numbers.sort(reverse=True)
    top_five_numbers = numbers[:5]

    print("The five greatest numbers in descending order are:")
    for num in top_five_numbers:
        print(num)

