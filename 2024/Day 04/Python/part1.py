import re

# mirror 2d array horizontally
def mirror(a):
  return [list(reversed(row)) for row in a]

# transpose 2d array
def transpose(a):
  return list(zip(*a))

# get / diagonals of 2d array
def get_forward_diagonals(a):
  size = len(a)
  diags = []
  for i in range(2 * size - 2, -1, -1):
    diag = []
    for j in range(i, -1, -1):
      if j < size and i - j < size:
        diag.append(a[j][i - j])
    diags.append(diag)
  return diags

# get \ diagonals of 2d array
def get_backward_diagonals(a):
  return get_forward_diagonals(mirror(a))

# count occurrences of XMAS and SAMX by row
def count_xmas(a):
  count = 0
  for row in a:
    count += len(re.findall("(?=(XMAS)|(SAMX))", "".join(row)))
  return count

# read input_data from file
with open("../input.txt", "r") as file:
  input_data = file.readlines()

# split input_data into 2d character array
arr = [list(line.strip()) for line in input_data]

total = 0
total += count_xmas(arr)                          # count occurrences in rows
total += count_xmas(transpose(arr))               # count occurrences in columns
total += count_xmas(get_forward_diagonals(arr))   # count occurrences in / diagonals
total += count_xmas(get_backward_diagonals(arr))  # count occurrences in \ diagonals

print(total)