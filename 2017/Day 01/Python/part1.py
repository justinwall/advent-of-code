# read input from file
with open("../input.txt", "r") as file:
  input_data = list(map(int, file.read()))

total = 0
size = len(input_data)
for i in range(size):
  current_value = input_data[i]
  next_value = input_data[(i + 1) % size]  # wrap back to the beginning on last iteration

  if current_value == next_value:
    total += current_value

print(total)