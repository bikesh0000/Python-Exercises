cabin_class = input("Enter the cabin class (LUX, A, B, or C): ")

if cabin_class == "LUX":
    print("Upper-deck balcony with cabin.")
elif cabin_class == "A":
    print("Above the car deck, equipped with window.")
elif cabin_class == "B":
    print("Windowless cabin above the car deck.")
elif cabin_class == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")Y