# depth-first search graph for if path exists from start to end
def dfs(graph, start, end, visited = None):
  if visited is None:
    visited = set()

  visited.add(start)

  # reached the end successfully
  if start == end:
    return True

  # haven't reached the end yet
  if start in graph.keys():
    for neighbor in graph[start]:
      if neighbor not in visited:
        if dfs(graph, neighbor, end, visited):  # advance along the path
          return True

  return False

# read input_data from file
with open("../input.txt", "r") as file:
  input_data = file.readlines()
grid = [list(map(int, list(line.strip()))) for line in input_data]  # convert to grid of numbers
width = len(grid[0])
height = len(grid)

# build directed graph k -> v where grid[v] = grid[k] + 1
graph = {}  # directed graph
zeros = []  # list of positions with 0
nines = []  # list of positions with 9
for i in range(height):
  for j in range(width):
    val = grid[i][j]

    if val == 0:
      zeros.append((i, j))
    if val == 9:
      nines.append((i, j))

    # if top neighbor in bounds and bigger by 1
    if i - 1 > -1 and grid[i - 1][j] == val + 1:
      if (i, j) not in graph.keys():
        graph[i, j] = [(i - 1, j)]
      else:
        graph[i, j] += [(i - 1, j)]

    # if bottom neighbor in bounds and bigger by 1
    if i + 1 < height and grid[i + 1][j] == val + 1:
      if (i, j) not in graph.keys():
        graph[i, j] = [(i + 1, j)]
      else:
        graph[i, j] += [(i + 1, j)]

    # if left neighbor in bounds and bigger by 1
    if j - 1 > -1 and grid[i][j - 1] == val + 1:
      if (i, j) not in graph.keys():
        graph[i, j] = [(i, j - 1)]
      else:
        graph[i, j] += [(i, j - 1)]

    # if right neighbor in bounds and bigger by 1
    if j + 1 < width and grid[i][j + 1] == val + 1:
      if (i, j) not in graph.keys():
        graph[i, j] = [(i, j + 1)]
      else:
        graph[i, j] += [(i, j + 1)]

# calculate total score for grid
total = 0
for trailhead in zeros:
  for trailend in nines:
    total += dfs(graph, trailhead, trailend)  # if path return 1, else return 0

print(total)