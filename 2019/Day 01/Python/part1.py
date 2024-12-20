import math

# read input from file
with open("../input.txt", "r") as file:
  input_data = list(map(int, file.readlines()))

total = 0
for mass in input_data:
  total += math.floor(mass / 3) - 2

print(total)