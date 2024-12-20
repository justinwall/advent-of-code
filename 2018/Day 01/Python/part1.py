# read input from file
with open("../input.txt", "r") as file:
  input_data = "".join(file.read().split('\n'))

print(eval(input_data))