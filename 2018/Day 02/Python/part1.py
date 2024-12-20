# read input from file
with open("../input.txt", "r") as file:
  input_data = file.readlines()

a = 0
b = 0

for line in input_data:
  twos = [ch for ch in line if line.count(ch) == 2]
  threes = [ch for ch in line if line.count(ch) == 3]
  a += len(twos) > 0
  b += len(threes) > 0

print(a * b)