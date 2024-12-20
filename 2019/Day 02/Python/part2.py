# read input from file
with open("../input.txt", "r") as file:
  input_data = list(map(int, file.read().strip().split(',')))

found = False
for x in range(100):
  for y in range(100):
    nums = input_data[:]
    nums[1] = x
    nums[2] = y

    i = 0
    while i in range(len(nums)) and nums[i] != 99:
      code = nums[i]
      pos1 = nums[i + 1]
      pos2 = nums[i + 2]
      pos3 = nums[i + 3]

      if code == 1:
        nums[pos3] = nums[pos1] + nums[pos2]
      elif code == 2:
        nums[pos3] = nums[pos1] * nums[pos2]

      i += 4

    if nums[0] == 19690720:
      found = True

    if found:
      break
  if found:
      break

print(100 * x + y)