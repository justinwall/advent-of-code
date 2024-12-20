# read input from file
with open("../input.txt", "r") as file:
  input_data = [list(map(int, line.strip().split())) for line in file.readlines()]

total = 0
for line in input_data:
  total += max(line) - min(line)

print(total)