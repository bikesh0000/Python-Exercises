gender = (input("Enter your gender (male/female) : "))
level = float(input("Enter your hameglobin level in gm/l: "))

#the program then notifies if the hameglobin level is low or high:

if gender == "female":
    if level < 117:
        print("You have a low level of hameglobin")
    elif level > 155:
        print("You have a high level of hameglobin")
    else:
        print("You have normal hameglobin level")

if gender == "male":
        if level < 134:
            print("You have a low level of hameglobin")
        elif level > 167:
            print("You have a high level of hameglobin")
        else:
            print("You have a normal hameglobin level")

else:
    print("Invalid input. Please enter male or female for gender.")

