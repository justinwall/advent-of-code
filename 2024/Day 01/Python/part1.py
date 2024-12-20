# read input_data from file
with open("../input.txt", "r") as file:
  input_data = file.readlines()

# columns to lists
a = []
b = []
for line in input_data:
  a.append(int(line.split()[0].strip()))
  b.append(int(line.split()[1].strip()))

a.sort()  # sort left column
b.sort()  # sort right column

total = 0
for i in range(0, len(a)):
  total += abs(b[i] - a[i])

print(total)