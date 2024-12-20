# read input from file
with open("../input.txt", "r") as file:
  input_data = list(map(int, file.read()))

total = 0
size = len(input_data)
for i in range(size):
  current_value = input_data[i]
  next_value = input_data[(i + size // 2) % size]  # keep index in [0, size)

  if current_value == next_value:
    total += current_value

print(total)