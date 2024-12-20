# read input from file
with open("../input.txt", "r") as file:
  input_data = [[x[0], x[1:]] for x in file.read().split(', ')]

# cycle of direction vectors
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
turn = 0  # mod 4 direction index

x = 0
y = 0
visited = [[x, y]]
visited_twice = None
for dir, steps in input_data:
  turn += 1 if dir == 'R' else -1

  for i in range(int(steps)):
    x += directions[turn % 4][0]
    y += directions[turn % 4][1]
    if [x, y] not in visited:
      visited.append([x, y])
    else:
      visited_twice = [x, y]
      break

  if visited_twice is not None:
    break

print(sum(list(map(abs, visited_twice))))