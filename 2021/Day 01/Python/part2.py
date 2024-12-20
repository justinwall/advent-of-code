import sys

# read input from file
with open("../input.txt", "r") as file:
  input_data = list(map(int, file.readlines()))

total = 0
prev_sum = sys.maxsize
for i in range(0, len(input_data) - 2):
  curr_sum = sum(input_data[i : i + 3])
  if curr_sum > prev_sum:
    total += 1
  prev_sum = curr_sum

print(total)
