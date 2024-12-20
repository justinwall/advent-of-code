# read input from file
with open("../input.txt", "r") as file:
  input_data = file.readlines()

presents = [sorted(list(map(int, line.strip().split('x')))) for line in input_data]

total = 0
for present in presents:
  paper = 2 * present[0] + 2 * present[1]
  ribbon = present[0] * present[1] * present[2]
  total += paper + ribbon

print(total)