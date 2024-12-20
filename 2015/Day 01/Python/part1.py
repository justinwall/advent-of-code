# read input from file
with open("../input.txt", "r") as file:
  input_data = list(file.read())

# +1 for each (, -1 for each )
floor = input_data.count('(') - input_data.count(')')

print(floor)