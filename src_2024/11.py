from utils.api import get_input

input_str = get_input(11)

# WRITE YOUR SOLUTION HERE
stones = [int(number) for number in input_str.split(' ')]
d = {}

def f(stone, k):
    if (stone, k) in d.keys():
        return d[(stone,k)]
    elif k == 0:
        d[(stone,k)] = 1
        return 1
    else:
        if stone == 0:
            d[(stone,k)] = f(1, k-1)
            return d[(stone,k)]
        else:
            stone_str = str(stone)
            a, b = divmod(len(stone_str), 2)
            if b == 0:
                d[(stone,k)] = f(int(stone_str[:a]), k-1) + f(int(stone_str[a:]), k-1)
                return d[(stone,k)]
            else:
                d[(stone,k)] = f(stone*2024, k-1)
                return d[(stone,k)]

# part 1
res = sum([f(stone, 25) for stone in stones])

print(f'part 1: {res}')

# part 2
res = sum([f(stone, 75) for stone in stones])

print(f'part 2: {res}')