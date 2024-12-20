# read input from file
with open("../input.txt", "r") as file:
  input_data = file.readlines()

digits = ([str(x) for x in range(10)] +
          ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])

total = 0
for line in input_data:
  # find lowest index of each digit in string
  left_indices = [[line.find(digits[i]), (i - 10) % 10] for i in range(len(digits))]
  # find highest index of each digit in string
  right_indices = [[line.rfind(digits[i]), (i - 10) % 10] for i in range(len(digits))]

  # remove digits not found and sort by index
  left_indices = sorted([x for x in left_indices if x[0] > -1], key=lambda x: x[0])
  right_indices = sorted([x for x in right_indices if x[0] > -1], key=lambda x: x[0])

  # concatenate first and last digit and add to total
  total += int(str(left_indices[0][1]) + str(right_indices[-1][1]))

print(total)