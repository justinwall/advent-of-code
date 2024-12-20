def contains_vowel(s):
  vowels = ['a', 'e', 'i', 'o', 'u']
  count = 0
  for ch in list(s):
    if ch in vowels:
      count += 1
    if count == 3:
      return True
  return False

def contains_double(s):
  s = list(s)
  for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
      return True
  return False

def contains_bad(s, bad):
  for term in bad:
    if s.find(term) != -1:
      return True
  return False

# read input from file
with open("../input.txt", "r") as file:
  input_data = file.readlines()

bad = ["ab", "cd", "pq", "xy"]

total = 0
for line in input_data:
  if contains_vowel(line) and contains_double(line) and not contains_bad(line, bad):
    total += 1

print(total)