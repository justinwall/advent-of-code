import itertools

# read input from file
with open("../input.txt", "r") as file:
  input_data = list(map(int, file.readlines()))

tuples = itertools.combinations(input_data, 3)  # get all possible 3-tuples of inputs
for tuple in tuples:
  a = tuple[0]
  b = tuple[1]
  c = tuple[2]
  if a + b + c == 2020:
    print(a * b * c)
    break