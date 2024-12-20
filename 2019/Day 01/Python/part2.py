import math

# recursively calculate fuel requirements
def calc_fuel(m):
  fuel = math.floor(m / 3) - 2
  if fuel <= 0:
    return 0
  return fuel + calc_fuel(fuel)

# read input from file
with open("../input.txt", "r") as file:
  input_data = list(map(int, file.readlines()))

total = 0
for mass in input_data:
  total += calc_fuel(mass)

print(total)