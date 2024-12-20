# read input_data from file
with open("../input.txt", "r") as file:
  input_data = file.readlines()

# split input_data into 2d character array
arr = [list(row.strip()) for row in input_data]

# frame of reference is 3x3 square with center from (1,1) to (n-1,n-1) for array of size n
# M . M  |  S . S  |  M . S  |  S . M
# . A .  |  . A .  |  . A .  |  . A .
# S . S  |  M . M  |  M . S  |  S . M
count = 0
for i in range(1, len(arr) - 1):
  for j in range(1, len(arr) - 1):
    if arr[i][j] == 'A':  # short circuit - center is A
      if ((arr[i-1][j-1] == 'M' and arr[i-1][j+1] == 'M' and arr[i+1][j-1] == 'S' and arr[i+1][j+1] == 'S') or  # M on top, S on bottom
          (arr[i+1][j-1] == 'M' and arr[i+1][j+1] == 'M' and arr[i-1][j-1] == 'S' and arr[i-1][j+1] == 'S') or  # M on bottom, S on top
          (arr[i-1][j-1] == 'M' and arr[i+1][j-1] == 'M' and arr[i-1][j+1] == 'S' and arr[i+1][j+1] == 'S') or  # M on left, S on right
          (arr[i-1][j+1] == 'M' and arr[i+1][j+1] == 'M' and arr[i-1][j-1] == 'S' and arr[i+1][j-1] == 'S')):   # M on right, S on left
        count += 1

print(count)