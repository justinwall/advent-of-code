# read input from file
with open("../input.txt", "r") as file:
  input_data = [list(line.strip()) for line in file.readlines()]

keypad = [['', '', '1', '', ''],
          ['', '2', '3', '4', ''],
          ['5', '6', '7', '8', '9'],
          ['', 'A', 'B', 'C', ''],
          ['', '', 'D', '', '']]
x = 0
y = 2

sequence = ""
for line in input_data:
  for instruction in line:
    match instruction:
      case 'U':
        if y - 1 in range(5) and keypad[y - 1][x] != '':
          y -= 1
      case 'R':
        if x + 1 in range(5) and keypad[y][x + 1] != '':
          x += 1
      case 'D':
        if y + 1 in range(5) and keypad[y + 1][x] != '':
          y += 1
      case 'L':
        if x - 1 in range(5) and keypad[y][x - 1] != '':
          x -= 1
  sequence += keypad[y][x]

print(sequence)