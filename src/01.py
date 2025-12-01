from utils.api import get_input

input_str = get_input(1)
# input_str = """L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82"""

# WRITE YOUR SOLUTION HERE

# part 1
dial_state = 50
num_at_zero = 0
for rotation in input_str.splitlines():
    # parse rotation
    try:
        direction = rotation[0]
        distance = int(rotation[1:])
        assert direction in ['L', 'R']
    except:
        raise ValueError(f'Could not parse rotation: {rotation}')
    if direction == 'L':
        distance = -distance
    old_dial_state = dial_state
    dial_state = (dial_state + distance) % 100
    if dial_state == 0:
        ended_at_zero_str = ' Ended at zero.'
        num_at_zero += 1
    else:
        ended_at_zero_str = ''
    print(f'{old_dial_state} rotated by {rotation} -> {old_dial_state + distance} -> {dial_state}.' + ended_at_zero_str)

print(f'The dial was {num_at_zero} times at the position 0 at the end of an rotation.')
print()

# part 2
dial_state = 50
num_at_zero = 0
for rotation in input_str.splitlines():
    # parse rotation
    try:
        direction = rotation[0]
        distance = int(rotation[1:])
        assert direction in ['L', 'R']
    except:
        raise ValueError(f'Could not parse rotation: {rotation}')
    
    if direction == 'L':
        distance = -distance
    
    old_dial_state = dial_state
    old_num_at_zero = num_at_zero
    
    dial_state = (old_dial_state + distance) % 100
    total_revolutions = abs(distance) // 100
    num_at_zero += total_revolutions
    if any([direction == 'R' and dial_state < old_dial_state,
            direction == 'L' and old_dial_state != 0 and dial_state > old_dial_state,
            direction == 'L' and dial_state == 0]):
        num_at_zero += 1
    if num_at_zero > old_num_at_zero:
        traversals = num_at_zero - old_num_at_zero
        traverse_zero_str = f' Traversed zero {'once' if traversals == 1 else str(traversals) + ' times'}.'
    else:
        traverse_zero_str = ''
    print(f'{old_dial_state} rotated by {rotation} -> {old_dial_state + distance} -> {dial_state}.' + traverse_zero_str)

print(f'The dial was {num_at_zero} times at the position 0 during or at the end of an rotation.')