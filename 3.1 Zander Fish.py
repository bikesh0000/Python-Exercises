#The fish size limit is 42 cm or longer
length = int(input("Enter the length of the Zander fish in cm: "))
if length < 42:
    print(f"The fish is {42 - length} cm the size limit. Please release the fish back to the sea")

else:
    print(f"Congrats! You caught the right size of the fish")