# read input from file
with open("../input.txt", "r") as file:
  input_data = [[x[0], x[1:]] for x in file.read().split(', ')]

# cycle of direction vectors
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
turn = 0  # mod 4 direction index

x = 0
y = 0
for dir, steps in input_data:
  turn += 1 if dir == 'R' else -1
  x += int(steps) * directions[turn % 4][0]
  y += int(steps) * directions[turn % 4][1]

print(x + y)