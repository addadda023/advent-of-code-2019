# Read input from file and store in mass
with open('day_1_input.txt') as f:
    mass = f.readlines()
    mass = [int(m.strip()) for m in mass]


def calculate_fuel(m):
    # Part 1
    # To find the fuel required for a module, take its mass,
    # divide by three, round down, and subtract 2
    return m//3-2


fuel = sum(calculate_fuel(m) for m in mass)
print(fuel)


def calculate_complete_fuel(m):
    # Part 2
    # Fuel needs its own fuel

    t_fuel = 0
    while m > 0:
        cur_fuel = calculate_fuel(m)
        if cur_fuel > 0:
            t_fuel += cur_fuel
        m = cur_fuel

    return t_fuel


total_fuel = sum(calculate_complete_fuel(m) for m in mass)
print(total_fuel)
