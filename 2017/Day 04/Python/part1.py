# read input from file
with open("../input.txt", "r") as file:
  input_data = [line.strip().split() for line in file.readlines()]

total = 0
for line in input_data:
  word_count = [line.count(word) for word in line]
  if max(word_count) == 1:
    total += 1

print(total)