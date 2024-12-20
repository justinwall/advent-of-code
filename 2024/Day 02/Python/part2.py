def check_safety(a):
  diffs = [a[i + 1] - a[i] for i in range(len(a) - 1)]    # build list of differences between consecutive pairs
  if (all(x < 0 and x in range(-3, 0) for x in diffs) or  # all differences are negative and between -3 and -1
      all(x > 0 and x in range(1, 4) for x in diffs)):    # all differences are positive and between 1 and 3
    return True
  else:
    return False

# read input_data from file
with open("../input.txt", "r") as file:
  input_data = file.readlines()

total = 0
for line in input_data:
  nums = [int(num.strip()) for num in line.split()]
  if check_safety(nums):
    total += 1  # report is safe
  else:
    for i in range(len(nums)):
      temp_nums = nums.copy()
      temp_nums.pop(i)
      if check_safety(temp_nums):
        total += 1  # report is safe by removing a single level
        break

print(total)