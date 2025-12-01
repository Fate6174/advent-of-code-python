from utils.api import get_input

input_str = get_input(13)

# WRITE YOUR SOLUTION HERE

def f(s : str, offset=0) -> int | None:
    a,b,p = s.splitlines()
    a1, a2 = a.split(',')
    a1, a2 = int(a1[12:]), int(a2[3:])
    b1, b2 = b.split(',')
    b1, b2 = int(b1[12:]), int(b2[3:])
    p1, p2 = p.split(',')
    p1, p2 = int(p1[9:]) + offset, int(p2[3:]) + offset
    det = a1*b2 - a2*b1
    n1 = b2 * p1 - b1 * p2
    n2 = -a2 * p1 + a1 * p2
    if n1 % det == 0 and n2 % det == 0:
        n1 = n1 // det
        n2 = n2 // det
        return 3*n1 + n2

# part 1
res = sum([machine_result for machine in input_str.split('\n\n') for machine_result in [f(machine)] if machine_result is not None])
print(f'part 1: {res}')

# part 2
res = sum([machine_result for machine in input_str.split('\n\n') for machine_result in [f(machine, 10000000000000)] if machine_result is not None])
print(f'part 2: {res}')