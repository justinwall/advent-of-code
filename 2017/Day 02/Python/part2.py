# read input from file
with open("../input.txt", "r") as file:
  input_data = [list(map(int, line.strip().split())) for line in file.readlines()]

total = 0
for line in input_data:
  for i in range(len(line) - 1):
    for j in range(i + 1, len(line)):
      a = line[i]
      b = line[j]
      if a % b == 0:
        total += a // b
      elif b % a == 0:
        total += b // a

print(total)