# build group starting at (i, j)
def get_group(grid, i, j, value):
  group = [(i, j)]

  # if cell outside grid bounds
  if i not in range(len(grid)):
    return []
  if j not in range(len(grid[0])):
    return []

  # if cell value not right
  if grid[i][j] != value:
    return []

  # if cell already in a group
  if visited[i][j]:
    return []

  visited[i][j] = True  # exclude cell from future groups

  group = group + get_group(grid, i + 1, j, value)  # cell below
  group = group + get_group(grid, i, j + 1, value)  # cell to right
  group = group + get_group(grid, i - 1, j, value)  # cell above
  group = group + get_group(grid, i, j - 1, value)  # cell to left

  return group

# calculate perimeter
def perimeter(group):
  perimeter = 0

  for point in group:
    i, j = point
    sides = 4

    # cell on right
    if (i, j + 1) in group:
      sides -= 1
    # cell on left
    if (i, j - 1) in group:
      sides -= 1
    # cell on top
    if (i - 1, j) in group:
      sides -= 1
    # cell on bottom
    if (i + 1, j) in group:
      sides -= 1

    perimeter += sides

  return perimeter

# read input_data from file
with open("../input.txt", "r") as file:
  input_data = file.readlines()
grid = [list(line.strip()) for line in input_data]  # convert to 2d grid of characters
height = len(grid)
width = len(grid[0])

# all cells unvisited at start
visited = [[False for j in range(width)] for i in range(height)]

# build list of groups
groups = []
for i in range(height):
  for j in range(width):
    if not visited[i][j]:  # start of new group
      groups.append(get_group(grid, i, j, grid[i][j]))

total = 0
for group in groups:
  p = perimeter(group)
  a = len(group)
  total += p * a

print(total)