import re

def contains_repeated_pair(s):
  return re.search(r'(\w\w).*?\1', s) != None

def contains_sandwiched_letter(s):
  return re.search(r'(\w).\1', s) != None

# read input from file
with open("../input.txt", "r") as file:
  input_data = file.readlines()

total = 0
for line in input_data:
  if contains_repeated_pair(line) and contains_sandwiched_letter(line):
    total += 1

print(total)