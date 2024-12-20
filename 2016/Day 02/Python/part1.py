# read input from file
with open("../input.txt", "r") as file:
  input_data = [list(line.strip()) for line in file.readlines()]

keypad = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9']]
x = 1
y = 1

sequence = ""
for line in input_data:
  for instruction in line:
    match instruction:
      case 'U':
        if y in [1, 2]:
          y -= 1
      case 'R':
        if x in [0, 1]:
          x += 1
      case 'D':
        if y in [0, 1]:
          y += 1
      case 'L':
        if x in [1, 2]:
          x -= 1
  sequence += keypad[y][x]

print(sequence)