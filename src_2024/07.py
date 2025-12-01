from utils.api import get_input
from typing import Callable

input_str = get_input(7)

# WRITE YOUR SOLUTION HERE
equations = [(int(a), [int(x) for x in b.split(' ')[1:]]) for line in input_str.splitlines() for a,b in [line.split(':')]]
def possible_results(equation_numbers : list[int], operators : list[Callable[[int, int], int]]) -> list[int]:
    possible_results = [equation_numbers[0]]
    equation_numbers = equation_numbers[1:]
    while len(equation_numbers) > 0:
        possible_results = [operator(x, equation_numbers[0]) for x in possible_results for operator in operators]
        equation_numbers = equation_numbers[1:]
    return possible_results

# part 1
add = lambda x, y: x+y
mul = lambda x, y: x*y
res = sum([
    equation_result for equation_result, equation_numbers in equations
        if equation_result in possible_results(equation_numbers, [add, mul])
    ])

print(f'part 1: {res}')

# part 2
concat = lambda x, y: int(str(x) + str(y))
res = sum([
    equation_result for equation_result, equation_numbers in equations
        if equation_result in possible_results(equation_numbers, [add, mul, concat])
    ])

print(f'part 2: {res}')