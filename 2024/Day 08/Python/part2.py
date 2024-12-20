import itertools

# check if position in bounds given width and height
def in_bounds(pos, w, h):
  i = pos[0]
  j = pos[1]
  return i in range(h) and j in range(w)

# read input_data from file
with open("../input.txt", "r") as file:
  input_data = [list(line.strip()) for line in file.readlines()]

# get grid dimensions
width = len(input_data[0])
height = len(input_data)

# antenna dictionary where k=frequency and v=list of positions
antennas = {}
for i in range(height):
  for j in range(width):
    freq, pos = input_data[i][j], [i, j]
    if freq != ".":
      if freq not in antennas.keys():
        antennas[freq] = [pos]
      else:
        antennas[freq].append(pos)

# build list of unique antinode positions
unique_antinodes = []
for frequency in antennas.keys():
  positions = antennas[frequency]
  pairs = list(itertools.combinations(positions, 2))  # get unique pairs of positions

  for pair in pairs:
    a = pair[0]
    b = pair[1]
    slope = [b[0] - a[0], b[1] - a[1]]  # slope from a to b

    antinodes = [a, b]  # a and b are both antinodes of each other

    # get antinodes moving away from a
    for i in itertools.count(start=1):
      antinode = [a[0] - i * slope[0], a[1] - i * slope[1]]
      if not in_bounds(antinode, width, height):
        break
      antinodes.append(antinode)

    # get antinodes moving away from b
    for i in itertools.count(start=1):
      antinode = [b[0] + i * slope[0], b[1] + i * slope[1]]
      if not in_bounds(antinode, width, height):
        break
      antinodes.append(antinode)

    for antinode in antinodes:
      if antinode not in unique_antinodes:
        unique_antinodes.append(antinode)

print(len(unique_antinodes))