# read input_data from file
with open("../input.txt", "r") as file:
  input_data = file.readlines()

# columns to lists
a = []
b = []
for line in input_data:
  a.append(int(line.split()[0].strip()))
  b.append(int(line.split()[1].strip()))

total = 0
for num in a:
  total += num * b.count(num)

print(total)