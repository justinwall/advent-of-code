# check if order of a follows rules in ref
def check_order(a, ref):
  while len(a) > 0:
    x = a.pop(-1)  # remove last element

    # if any remaining values in a should come after x
    if len([y for y in a if y in ref[x]]) > 0:
      return False
  return True

# rearrange order of a according to rules in ref
def correct_order(a, ref, result):
  x = a[-1]                          # last element in a
  y = [n for n in a if n in ref[x]]  # elements in a that should be after x

  # case 1 - at least one element in a should be after x but isn't
  for z in y:
    a.remove(z)
    a.append(z)

  # case 2 - no elements in a should be after x - shrink problem size
  if y == []:
    a.remove(x)
    result.insert(0, x)

  while len(a) > 0:
    correct_order(a, ref, result)

  return result

# read input_data from file
with open("../input.txt", "r") as file:
  first_section, second_section = file.read().split('\n\n')
rules = first_section.strip().split('\n')
pagesets = second_section.strip().split('\n')

# create dictionary where k=page and v=list of pages that come after k
rule_dict = {}
for rule in rules:
  k, v = list(map(int, rule.split('|')))
  if k not in rule_dict.keys():
    rule_dict[k] = [v]
  else:
    rule_dict[k].append(v)
  if v not in rule_dict.keys():
    rule_dict[v] = []

total = 0
for pageset in pagesets:
  pageset = list(map(int, pageset.split(',')))
  if not check_order(pageset[:], rule_dict):            # if order is incorrect
    pageset = correct_order(pageset[:], rule_dict, [])  # correct the order
    total += pageset[len(pageset) // 2]                 # add middle page

print(total)