# Input the initial temperature of the body at the time of death
temperature_0 = float(input("Enter the temperature of the body at the time of death (in Celsius): "))

# Calculate the temperatures for 1 to 4 hours after death using the provided formula
temperature_1 = temperature_0 + (27 - temperature_0) * 0.2
temperature_2 = temperature_1 + (27 - temperature_1) * 0.2
temperature_3 = temperature_2 + (27 - temperature_2) * 0.2
temperature_4 = temperature_3 + (27 - temperature_3) * 0.2

# Print the temperatures from 1 to 4 hours after death
print(temperature_1)
print(temperature_2)
print(temperature_3)
print(temperature_4)
