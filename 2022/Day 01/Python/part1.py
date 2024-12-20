# read input from file
with open("../input.txt", "r") as file:
  input_data = file.read()
elves = input_data.split('\n\n')

most = 0
for elf in elves:
  total = sum(list(map(int, elf.split('\n'))))
  if total > most:
    most = total

print(most)