#Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.

a = 1
while  a < 1000:
    if a % 3 == 0:
        print (a)
    a += 1