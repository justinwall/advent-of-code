from math import floor
from itertools import repeat

# read input_data from file
with open("../input.txt", "r") as file:
  input_data = file.read()
disk_map = list(map(int, input_data.strip()))

# convert disk_map to memory list
memory = []
block = 0
for i in range(len(disk_map)):
  if i % 2 == 0:
    memory += list(repeat(int(block), disk_map[i]))
  else:
    memory += list(repeat('.', disk_map[i]))
  block += .5

num_idx = [i for i in range(len(memory) - 1, -1, -1) if memory[i] != '.']
for idx in num_idx:
  # if gap left of number, swap them
  gap = memory.index('.')
  if gap < idx:
    memory[idx], memory[gap] = memory[gap], memory[idx]

# calculate checksum
total = 0
for i in range(len(memory)):
  val = memory[i]
  if val != '.':
    total += i * val

print(total)