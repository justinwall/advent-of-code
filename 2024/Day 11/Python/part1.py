# apply three stone rules to n for i levels of depth with memoization
def apply_rules(n, i, memo = None):
  if memo is None:
    memo = {}

  if i == 0:
    return 1  # on last iteration, each stone counts as 1
  i = i - 1

  if (n, i) in memo:
    return memo[n, i]  # use cached result

  # rule 1
  if n == 0:
    result = apply_rules(1, i, memo)
    memo[n, i] = result
    return result

  # rule 2
  n_str = str(n)
  n_len = len(n_str)
  if n_len % 2 == 0:  # rule 2
    left = int(n_str[:n_len // 2])
    right = int(n_str[n_len // 2:])
    result = apply_rules(left, i, memo) + apply_rules(right, i, memo)
    memo[n, i] = result
    return result

  # rule 3
  result = apply_rules(n * 2024, i, memo)
  memo[n, i] = result
  return result

# read input_data from file
with open("../input.txt", "r") as file:
  input_data = file.read().strip()
stones = list(map(int, input_data.split()))  # convert to list of nums

stone_count = 0
for stone in stones:
  # add number of stones it turns into after 25 iterations
  stone_count += apply_rules(stone, 25)

print(stone_count)