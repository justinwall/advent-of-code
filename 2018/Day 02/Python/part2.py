# read input from file
with open("../input.txt", "r") as file:
  input_data = [list(line.strip()) for line in file.readlines()]

for line1 in input_data:
  for line2 in input_data:
    matches = [(x, y) for x, y in list(zip(line1, line2)) if x == y]
    if len(matches) == len(line1) - 1:
      match, match = list(zip(*matches))

print("".join(match))