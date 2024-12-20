def is_valid(t):
  return ((t[0] + t[1] > t[2]) and
          (t[1] + t[2] > t[0]) and
          (t[0] + t[2] > t[1]))

# read input from file
with open("../input.txt", "r") as file:
  input_data = [list(map(int, line.strip().split())) for line in file.readlines()]

total = 0
for triangle in input_data:
  total += is_valid(triangle)

print(total)