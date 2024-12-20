# read input_data from file
with open("../input.txt", "r") as file:
  input_data = file.readlines()

# split input_data into 2d character array
arr = [list(row.strip()) for row in input_data]

# frame of reference is 4x4 square with top left corner from (0,0) to (n-4,n-4) for array of size n
terms = []
for i in range(0, len(arr)):
  for j in range(0, len(arr)):
    if i <= len(arr) - 4:
      terms.append("".join([arr[i][j],arr[i+1][j],arr[i+2][j],arr[i+3][j]]))          # vertical term
    if j <= len(arr) - 4:
      terms.append("".join([arr[i][j],arr[i][j+1],arr[i][j+2],arr[i][j+3]]))          # horizontal term
      if i >= 3:
        terms.append("".join([arr[i][j],arr[i-1][j+1],arr[i-2][j+2],arr[i-3][j+3]]))  # / term
    if j >= 3 and i >= 3:
      terms.append("".join([arr[i][j],arr[i-1][j-1],arr[i-2][j-2],arr[i-3][j-3]]))    # \ term

total = 0
total += terms.count("XMAS")
total += terms.count("SAMX")

print(total)