import itertools

# read input from file
with open("../input.txt", "r") as file:
  input_data = list(map(int, file.readlines()))

pairs = itertools.combinations(input_data, 2)  # get all possible pairs of inputs
for pair in pairs:
  a = pair[0]
  b = pair[1]
  if a + b == 2020:
    print(a * b)
    break