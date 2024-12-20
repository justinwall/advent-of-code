# read input from file
with open("../input.txt", "r") as file:
  input_data = list(file.read().strip())

houses = {"0,0": 2}
s_x = 0
s_y = 0
r_x = 0
r_y = 0

for i in range(len(input_data)):
  if input_data[i] == "^":
    if i % 2 == 0:
      s_y += 1
    else:
      r_y += 1
  elif input_data[i] == ">":
    if i % 2 == 0:
      s_x += 1
    else:
      r_x += 1
  elif input_data[i] == "v":
    if i % 2 == 0:
      s_y -= 1
    else:
      r_y -= 1
  else:
    if i % 2 == 0:
      s_x -= 1
    else:
      r_x -= 1
  
  s_pos = str(s_x) + "," + str(s_y)
  if s_pos in houses.keys():
    houses[s_pos] += 1
  else:
    houses[s_pos] = 1

  r_pos = str(r_x) + "," + str(r_y)
  if r_pos in houses.keys():
    houses[r_pos] += 1
  else:
    houses[r_pos] = 1

print(len(houses))