from collections import deque

# bfs shortest path function
def shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        (row, col), path = queue.popleft()

        if (row, col) == end:
            return path + [(row, col)]

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = row + dr, col + dc
            if r in range(rows) and c in range(cols) and grid[r][c] == 0 and (r, c) not in visited:
                queue.append(((r, c), path + [(row, col)]))
                visited.add((r, c))

    return None

# read input_data from file
with open("../input.txt", "r") as file:
    obstacles = [line.strip() for line in file.readlines()]

grid_size = 71
obstacle_count = 1024
grid = [[0 for j in range(grid_size)] for i in range(grid_size)]
for i in range(obstacle_count):
    row, col = list(map(int, obstacles[i].split(',')))
    grid[row][col] = 1

# number of steps is length of shortest path minus the initial node
path = shortest_path(grid, (0, 0), (grid_size - 1, grid_size - 1))
print(len(path) - 1)