from utils.api import get_input

input_str = get_input(5)

# WRITE YOUR SOLUTION HERE
sep_idx = input_str.find('\n\n')
rules = [(int(item[:2]), int(item[3:])) for item in input_str[:sep_idx].splitlines()]
updates = [[int(x) for x in item.split(',')] for item in input_str[sep_idx+2:].splitlines()]

def sort(rules : list[tuple[int,int]]) -> list[int]:
    out = []
    while len(rules) > 1:
        smallest_numbers = {a for a,b in rules} - {b for a,b in rules}
        if len(smallest_numbers) != 1:
            raise RuntimeError(f'No unique minimum in {rules}.')
        smallest_number = smallest_numbers.pop()
        out += [smallest_number]
        rules = [item for item in rules if item[0] != smallest_number]
    out += [rules[0][0], rules[0][1]]
    return out

# part 1
res = 0
for update in updates:
    relevant_rules = [item for item in rules if item[0] in update and item[1] in update]
    local_order = sort(relevant_rules)
    if update == local_order:
        res += update[len(update) // 2]

print(f'part1: {res}')

# part 2
res = 0
for update in updates:
    relevant_rules = [item for item in rules if item[0] in update and item[1] in update]
    local_order = sort(relevant_rules)
    if update != local_order:
        res += local_order[len(local_order) // 2]

print(f'part2: {res}')