#Write a program that draws two random combinations of numbers for a combination lock:
#a 3-digit code where each number is between 0 and 9.

import random
code1 = ""
count = 0
while count < 3:
    digit = random.randint(0,9)
    code1 += str(digit)
    count += 1

count = 0
code2 = ""
while count < 3:
    digit = random.randint(0,9)
    code2 += str(digit)
    count += 1

print(f"The first random 3 digit code {code1}")
print(f"The second random 3 digit code {code2}")