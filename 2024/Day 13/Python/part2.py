from re import findall

# read input_data from file
with open("../input.txt", "r") as file:
  input_data = file.read().split('\n\n')

# each case is a system of two equations
# ax * a + bx * b = px
# ay * a + by * b = py
total = 0
for case in input_data:
  ax, ay, bx, by, px, py = map(int, findall(r"\d+", case))

  px += 1e13
  py += 1e13

  # solve for a (nearest integer)
  a = round((py / by - px / bx) /
            (ay / by - ax / bx))

  # back-solve for b (nearest integer)
  b = round((px - a * ax) /
                 bx)

  # verify result (removes cases where solution wasn't integers)
  if (a * ax + b * bx == px and
      a * ay + b * by == py):
    total += 3 * a + b

print(total)