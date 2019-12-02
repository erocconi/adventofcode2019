import math

def get_fuel(mass):
    fuel_req = (math.floor(mass / 3)) - 2
    return fuel_req

file = 'Day1-Input.txt'
mass = 0
with open(file) as input:
    for line in input:
        fuel_req = 0
        int_input = int(line)
        fuel_check = get_fuel(int_input)
        while fuel_check > 0:
            fuel_req += fuel_check
            fuel_check = get_fuel(fuel_check)
        mass += fuel_req
print("Total Mass Required: {} units".format(mass))