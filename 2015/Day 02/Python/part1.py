# read input from file
with open("../input.txt", "r") as file:
  input_data = file.readlines()

presents = [sorted(list(map(int, line.strip().split('x')))) for line in input_data]

total = 0
for present in presents:
  a = present[0]
  b = present[1]
  c = present[2]

  paper = (2 * a * b) + (2 * a * c) + (2 * b * c) + (a * b)
  total += paper

print(total)