# read input from file
with open("../input.txt", "r") as file:
  input_data = file.readlines()

total = 0
for line in input_data:
  digits = [x for x in list(line) if x.isnumeric()]  # get digits from line
  total += int(digits[0] + digits[-1])  # concatenate first and last digit

print(total)