import itertools

# read input from file
with open("../input.txt", "r") as file:
  input_data = file.readlines()

size = len(input_data)  # number of frequency changes

frequency = 0
frequencies = []
for i in itertools.count():
  frequency = eval(str(frequency) + input_data[i % size])  # circle back to beginning if no duplicate found
  if frequency in frequencies:
    break
  frequencies.append(frequency)

print(frequency)