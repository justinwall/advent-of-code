import itertools
import hashlib

# read input from file
with open("../input.txt", "r") as file:
  input_data = file.read().strip()

for i in itertools.count():
  encoded = hashlib.md5((input_data + str(i)).encode())
  if encoded.hexdigest().startswith('00000'):
    print(i)
    break