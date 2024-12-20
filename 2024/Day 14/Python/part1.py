from re import findall
from math import prod

# read input data from file
with open("../input.txt", "r") as file:
  robots = file.readlines()
width = 101
height = 103
x_mid = width // 2
y_mid = height // 2

# hashmap of all possible positions initialized to 0 count
facility = {}
for i in range(width):
  for j in range(height):
    facility[i, j] = 0

for robot in robots:
  p_x, p_y, v_x, v_y = map(int, findall(r"-?\d+", robot))

  # run 100 iterations
  p_x = (p_x + 100 * v_x) % width
  p_y = (p_y + 100 * v_y) % height

  # record final position of robot
  facility[p_x, p_y] += 1

quadrants = [0, 0, 0, 0]
for position in facility.keys():
  x = position[0]
  y = position[1]
  count = facility[x, y]

  # quadrants going clockwise starting in top left
  if count > 0:
    if x < x_mid and y < y_mid:
      quadrants[0] += count
    elif x > x_mid and y < y_mid:
      quadrants[1] += count
    elif x > x_mid and y > y_mid:
      quadrants[2] += count
    elif x < x_mid and y > y_mid:
      quadrants[3] += count

# output product of quadrant counts
print(prod(quadrants))