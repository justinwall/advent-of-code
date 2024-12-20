# read input from file
with open("../input.txt", "r") as file:
  input_data = file.read()
nums = list(map(int, input_data.strip().split(',')))

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

print(nums[0])