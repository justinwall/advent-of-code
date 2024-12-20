def is_valid(t):
  return ((t[0] + t[1] > t[2]) and
          (t[1] + t[2] > t[0]) and
          (t[0] + t[2] > t[1]))

# read input from file
with open("../input.txt", "r") as file:
  input_data = [list(map(int, line.strip().split())) for line in file.readlines()]

total = 0
for i in range(0, len(input_data), 3):
  t_one = [input_data[i][0], input_data[i + 1][0], input_data[i + 2][0]]
  t_two = [input_data[i][1], input_data[i + 1][1], input_data[i + 2][1]]
  t_three = [input_data[i][2], input_data[i + 1][2], input_data[i + 2][2]]

  total += is_valid(t_one) + is_valid(t_two) + is_valid(t_three)

print(total)