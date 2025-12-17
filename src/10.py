from utils.api import get_input
from time import time
import numpy as np
import scipy.optimize as sciopt
from math import lcm
np.set_printoptions(linewidth=150)

input_str = get_input(10)
# input_str = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
# """

# WRITE YOUR SOLUTION HERE

# part 1
tic = time()
out = 0
for line in input_str.splitlines():
    a, b = line.split(']')
    target = sum([2 ** idx for idx, c in enumerate(a[1:]) if c == '#'])
    c, d = b.split('{')
    buttons = [sum([2 ** int(num) for num in button[1:-1].split(',')]) for button in c.strip().split(' ')]
    joltage = [int(jolt) for jolt in d[:-1].split(',')]
    num_presses = len(buttons)
    for i in range(2 ** len(buttons)):
        num = 0
        j = i
        for button in buttons:
            if j % 2 > 0:
                num = num ^ button
            j = j // 2
        if num == target:
            num_presses = min(num_presses, i.bit_count())
    out += num_presses
toc = time()
print(f'{toc-tic:.6f} secs: {out}')

# part 2
tic = time()
out = 0
for idx, line in enumerate(input_str.splitlines()):
    a, b = line.split(']')
    c, d = b.split('{')
    buttons = [[int(num) for num in button[1:-1].split(',')] for button in c.strip().split(' ')]
    joltage = [int(jolt) for jolt in d[:-1].split(',')]
    # set up mixed integer linear programming
    c = np.ones(len(buttons), dtype=int)
    A = np.zeros((len(joltage), len(buttons)+1), dtype=int)
    for i, button in enumerate(buttons):
        for j in button:
            A[j, i] = 1
    A[:,-1] = joltage
    
    ########################################################################
    # Using a general MILP solver
    # constraints = [sciopt.LinearConstraint(A[idx:idx+1,:-1], lb=jolt, ub=jolt) for idx, jolt in enumerate(joltage)]
    # milp_result = sciopt.milp(c, integrality=np.ones(len(buttons), dtype=int), constraints=constraints)
    # out += int(sum(milp_result.x))
    ########################################################################
    
    ########################################################################
    # Iterating through possible solutions, finding the desired minimum
    # Find upper bounds for all variables
    max_values = []
    for j in range(len(buttons)):
        indices = np.argwhere(A[:,j] != 0)
        max_values.append(np.min(A[indices,-1] // A[indices,j]))
    max_values = np.array(max_values)
    
    # Process the matrix with the Gaussian algorithm, and
    # identify the independent (free) variables
    free_variables = []
    A_diag = []
    for j in range(len(buttons)):
        diag_idx = j - len(free_variables)
        # search for first nonzero column entry starting from the diagonal
        found = -1
        for i in range(diag_idx, len(joltage)):
            if A[i,j] != 0:
                found = i
                break
        if found < 0:
            # if there is no nonzero element after the diagonal,
            # this variable is an independent variable.
            free_variables.append(j)
        else:
            # else switch the j-th and found-th row
            # and eliminate all other column entries (except
            # the j-th) using the j-th column entry
            if found != diag_idx:
                A[[diag_idx,found]] = A[[found,diag_idx]]
            for i in range(len(joltage)):
                if i != diag_idx and A[i,j] != 0:
                    kgv = lcm(A[diag_idx,j], A[i, j])
                    A[i,:] = kgv // A[i,j] * A[i,:] - kgv // A[diag_idx,j] * A[diag_idx, :]
            A_diag.append((diag_idx,j))
    # Now, only the diagonal of dependent variables and the
    # columns of the free variables are needed.
    A_diag = np.array([A[i,j] for i,j in A_diag])
    free_variables = np.array(free_variables, dtype=int)
    print((idx, free_variables))
    A_free = A[:len(A_diag), free_variables]
    rhs = A[:len(A_diag),-1]
    max_values = max_values[free_variables]
    # The increments are the steps that any free
    # variable needs to change to get from one possible
    # solution to the next one, if all other free
    # variables stay constant.
    increments = np.lcm.reduce(np.abs(A_diag)[:,None] // np.gcd(A_free, A_diag[:,None]))

    # Identify the free variable with the maximum value
    # of (increment, max_value).
    max_step_idx = 0
    for idx in range(len(free_variables)):
        if (increments[idx], max_values[idx]) > (increments[max_step_idx], max_values[max_step_idx]):
            max_step_idx = idx
    # Put this variable to the front.
    if max_step_idx > 0:
        A_free[:, [0, max_step_idx]] = A_free[:, [max_step_idx, 0]]
        max_values[[0, max_step_idx]] = max_values[[max_step_idx, 0]]
        increments[[0, max_step_idx]] = increments[[max_step_idx, 0]]

    # Iterate through values of the free variables.
    sol_min = 1000000000000000000000000000
    free_variables = np.zeros(len(free_variables), dtype=int)
    consistent = False
    while True:
        # solve the system for the current state of the free variables
        val = rhs - A_free @ free_variables
        if consistent or np.all(val % A_diag == 0):
            consistent = True
            sol = val // A_diag
            if np.all(sol >= 0):
                sol_min = min(sol_min, np.sum(sol) + np.sum(free_variables))
        # advance the state of the free variables
        for i in range(len(free_variables)):
            if consistent:
                if free_variables[i] + increments[i] <= max_values[i]:
                    free_variables[i] += increments[i]
                    break
                else:
                    free_variables[i] = 0
                    consistent = False
            else:
                if free_variables[i] < max_values[i]:
                    free_variables[i] += 1
                    break
                else:
                    free_variables[i] = 0
        if np.all(free_variables == 0):
            break
    out += sol_min
    ########################################################################

toc = time()
print(f'{toc-tic:.6f} secs: {out}')