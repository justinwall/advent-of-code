# move the robot and update the facility map
def move_robot(fmap, rx, ry, dx, dy):
    rx_t = rx + dx
    ry_t = ry + dy

    # if next robot position is a wall, don't move
    if fmap[ry_t][rx_t] == '#':
        return rx, ry

    # if next robot position is empty, move there
    if fmap[ry_t][rx_t] == '.':
        fmap[ry][rx] = '.'
        fmap[ry_t][rx_t] = '@'
        return rx_t, ry_t

    # otherwise, next robot position is a box
    # find the next available non-box position in this direction
    next_x = rx_t
    next_y = ry_t
    while fmap[next_y][next_x] == 'O':
        next_x += dx
        next_y += dy

    # if the next available non-box positions is empty,
    # then move robot and boxes
    if fmap[next_y][next_x] == '.':
        # if moving horizontally, shift all boxes horizontally
        if dy == 0:
            for i in range(next_x, rx, -1 * dx):
                fmap[ry][i] = 'O'

        # if moving vertically, shift all boxes vertically
        if dx == 0:
            for i in range(next_y, ry, -1 * dy):
                fmap[i][rx] = 'O'

        # move the robot over once
        fmap[ry_t][rx_t] = '@'
        fmap[ry][rx] = '.'
        return rx_t, ry_t

    # if next available non-box position is a wall,
    # then don't move anything
    return rx, ry

# print state of map to console
def print_map(fmap):
    for row in fmap:
        print("".join(row))
    print()

# read input_data from file
with open("../input.txt", "r") as file:
    input_data = file.read().strip().split('\n\n')

# split input_data into 2d array for facility map and list for robot moves
facility = [list(row) for row in input_data[0].split('\n')]
robot_moves = [x for x in list(input_data[1]) if x != '\n']

facility_height = len(facility)
facility_width = len(facility[0])

# find the robot's initial position
found = False
for i in range(facility_height):
    for j in range(facility_width):
        if facility[i][j] == '@':
            found = True
            break
    if found:
        break

rx = j
ry = i
for move in robot_moves:
    # determine the delta movement based on instruction
    if move == '<':
        dx, dy = [-1, 0]
    elif move == '>':
        dx, dy = [1, 0]
    elif move == '^':
        dx, dy = [0, -1]
    elif move == 'v':
        dx, dy = [0, 1]

    rx, ry = move_robot(facility, rx, ry, dx, dy)

# calculate sum of GPS coordinates
# 100 times its distance from the top edge
# plus its distance from the left edge of the map
total = 0
for i in range(facility_height):
    for j in range(facility_width):
        if facility[i][j] == 'O':
            total += 100 * i + j

# print final map state and the answer
print_map(facility)
print(total)