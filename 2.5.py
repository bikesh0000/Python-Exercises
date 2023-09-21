# Conversion factors
POUNDS_PER_TALENT = 20
LOTS_PER_POUND = 32
GRAMS_PER_LOT = 13.3

talents = float(input("Enter the mass in talents: "))
pounds = float(input("Enter the mass in pounds: "))
lots = float(input("Enter the mass in lots: "))

# Calculate the total mass in lots
total_lots = (talents * POUNDS_PER_TALENT * LOTS_PER_POUND) + (pounds * LOTS_PER_POUND) + lots

# Convert to kilograms and grams
total_kilograms = total_lots * (GRAMS_PER_LOT / 1000)
total_grams = (total_kilograms - int(total_kilograms)) * 1000

# Display the result
print(f"The mass is equivalent to {int(total_kilograms)} kilograms and {int(total_grams)} grams.")
