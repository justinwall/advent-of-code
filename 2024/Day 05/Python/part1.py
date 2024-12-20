# check if order of a follows rules in ref
def check_order(a, ref):
  while len(a) > 0:
    x = a.pop(-1)  # remove last element

    # if any remaining values in a should come after x
    if len([y for y in a if y in ref[x]]) > 0:
      return False
  return True

# read input_data from file
with open("../input.txt", "r") as file:
  first_section, second_section = file.read().split('\n\n')
rules = first_section.strip().split('\n')
pagesets = second_section.strip().split('\n')

# create dictionary where k=page and v=list of pages that come after k
rule_tree = {}
for rule in rules:
  k, v = list(map(int, rule.split('|')))
  if k not in rule_tree.keys():
    rule_tree[k] = [v]
  else:
    rule_tree[k].append(v)
  if v not in rule_tree.keys():
    rule_tree[v] = []

total = 0
for pageset in pagesets:
  pageset = list(map(int, pageset.split(',')))
  if check_order(pageset[:], rule_tree):        # if order is correct
    total += pageset[len(pageset) // 2]         # add middle page

print(total)