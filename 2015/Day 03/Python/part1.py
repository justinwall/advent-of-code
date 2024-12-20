# read input from file
with open("../input.txt", "r") as file:
  input_data = list(file.read().strip())

houses = {"0,0": 1}
x = 0
y = 0

for instruction in input_data:
  if instruction == "^":
    y += 1
  elif instruction == ">":
    x += 1
  elif instruction == "v":
    y -= 1
  else:
    x -= 1
  
  position = str(x) + "," + str(y)
  if position in houses.keys():
    houses[position] += 1
  else:
    houses[position] = 1

print(len(houses))