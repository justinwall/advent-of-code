# read input from file
with open("../input.txt", "r") as file:
  input_data = list(map(int, file.readlines()))

total = 0
for i in range(len(input_data) - 1):
  if input_data[i + 1] > input_data[i]:
    total += 1

print(total)
