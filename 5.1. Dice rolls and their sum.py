#Write a program that asks the user how many dice to roll.
# The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.

import random
rolls = int(input("how many dice to roll?: "))
total_sum = 0

for _ in range(rolls):
    rolls_result = random.randint(0,6)
    total_sum += rolls_result

print(f"The total sum of the rolls of {rolls} dice is {total_sum}")
