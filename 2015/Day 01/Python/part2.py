# read input from file
with open("../input.txt", "r") as file:
  input_data = list(file.read())

floor = 0
position = 0
while floor >= 0:
  floor += 1 if input_data[position] == '(' else -1
  position += 1

print(position)