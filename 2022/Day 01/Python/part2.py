# read input from file
with open("../input.txt", "r") as file:
  input_data = file.read()
elves = input_data.split('\n\n')

# sort elves by total carried
totals = sorted([sum(list(map(int, elf.split('\n')))) for elf in elves])

print(sum(totals[-3:]))  # print sum of highest three