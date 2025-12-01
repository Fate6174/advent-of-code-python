from utils.api import get_input

input_str = get_input(19)

# WRITE YOUR SOLUTION HERE
patterns, designs = input_str.split('\n\n')
patterns = patterns.split(', ')
designs = designs.splitlines()

design_dict = {'': 1}

def f(design : str) -> int:
    if design not in design_dict.keys():
        design_dict[design] = 0
        for pattern in patterns:
            if design.startswith(pattern):
                design_dict[design] = design_dict[design] + f(design[len(pattern):])
    return design_dict[design]

# part 1
res = sum([1 for design in designs if f(design) > 0])
print(f'part 1: {res}')

# part 2
res = sum([f(design) for design in designs])
print(f'part 2: {res}')