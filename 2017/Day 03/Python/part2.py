with open("../input.txt", "r") as file:
  input_data = int(file.read().strip())

x = 0
y = 0
n = 1

directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
turn = 0
step = 1

grid = {(x, y): n}

while n < input_data:
  for i in range(2):
    d = directions[turn % 4]
    for j in range(step):
      x += d[0]
      y += d[1]

      n = 0
      if (x - 1, y - 1) in grid.keys():
        n += grid[(x - 1, y - 1)]
      if (x - 1, y) in grid.keys():
        n += grid[(x - 1, y)]
      if (x - 1, y + 1) in grid.keys():
        n += grid[(x - 1, y + 1)]
      if (x, y + 1) in grid.keys():
        n += grid[(x, y + 1)]
      if (x + 1, y + 1) in grid.keys():
        n += grid[(x + 1, y + 1)]
      if (x + 1, y) in grid.keys():
        n += grid[(x + 1, y)]
      if (x + 1, y - 1) in grid.keys():
        n += grid[(x + 1, y - 1)]
      if (x, y - 1) in grid.keys():
        n += grid[(x, y - 1)]

      grid[(x, y)] = n

      if n > input_data:
        break
    if n > input_data:
      break
    turn += 1
  step += 1

print(n)