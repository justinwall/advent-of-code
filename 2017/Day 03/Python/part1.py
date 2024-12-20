with open("../input.txt", "r") as file:
  input_data = int(file.read().strip())

x = 0
y = 0
n = 1
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
turn = 0
step = 1

grid = [[1]]

while n < input_data:
  for i in range(2):
    d = directions[turn % 4]
    for j in range(step):
      n += 1
      x += d[0]
      y += d[1]
      if n == input_data:
        break
    if n == input_data:
      break
    turn += 1
  step += 1

print(abs(x) + abs(y))
print(grid)