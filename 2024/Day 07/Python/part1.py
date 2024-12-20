# build list of all possible results
def calculate(nums):
  if len(nums) == 1:
    return nums

  return (calculate([nums[0] + nums[1]] + nums[2:]) +  # add
          calculate([nums[0] * nums[1]] + nums[2:]))   # multiply

# read input_data from file
with open("../input.txt", "r") as file:
  input_data = file.readlines()

total = 0
for line in input_data:
  left, right = line.split(": ")
  result = int(left)
  operands = list(map(int, right.split()))

  # get results of all possible operand/operator combinations
  results = calculate(operands)

  # if one of the possible results is correct
  if result in results:
    total += result  # add it to the total

print(total)