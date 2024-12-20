import re

# read input_data from file
with open("../input.txt", "r") as file:
  input_data = file.read()

matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input_data)  # extract tuples of numbers to multiply
print(sum([int(match[0])*int(match[1]) for match in matches]))
