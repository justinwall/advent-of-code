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

# check for first obstacle that prevents a path
grid_size = 71
grid = [[0 for j in range(grid_size)] for i in range(grid_size)]
for i in range(len(obstacles)):
    row, col = list(map(int, obstacles[i].split(',')))
    grid[row][col] = 1
    path = shortest_path(grid, (0, 0), (grid_size - 1, grid_size - 1))

    # no path, obstacles[i] is the blocking obstacle
    if path is None:
        break

print(obstacles[i])