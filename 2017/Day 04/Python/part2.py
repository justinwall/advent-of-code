# read input from file
with open("../input.txt", "r") as file:
  input_data = [line.strip().split() for line in file.readlines()]

total = 0
for line in input_data:
  invalid = False

  i = 0
  while i in range(len(line)) and not invalid:
    j = 0
    while j in range(len(line)) and not invalid:
      if i != j and sorted(line[i]) == sorted(line[j]):
        invalid = True

      j += 1

    i += 1

  if not invalid:
    total += 1

print(total)