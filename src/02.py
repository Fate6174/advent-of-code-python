from utils.api import get_input

input_str = get_input(2)
# input_str = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

# WRITE YOUR SOLUTION HERE

# part 1
sum_invalid_ids = 0
id_ranges = input_str.split(',')
for id_range in id_ranges:
    start, stop = id_range.split('-')
    for num in range(int(start), int(stop)+1):
        num_str = str(num)
        num_str_len = len(num_str)
        if num_str_len % 2 == 0:
            half_length = num_str_len // 2
            if num_str[:half_length] == num_str[half_length:]:
                sum_invalid_ids += num

print(sum_invalid_ids)

# part 2
sum_invalid_ids = 0
id_ranges = input_str.split(',')
for id_range in id_ranges:
    start, stop = id_range.split('-')
    for num in range(int(start), int(stop)+1):
        num_str = str(num)
        num_str_len = len(num_str)
        for num_parts in range(2,num_str_len+1):
            if num_str_len % num_parts == 0:
                part_length = num_str_len // num_parts
                first_part = num_str[:part_length]
                if all([first_part == num_str[idx*part_length:(idx+1)*part_length] for idx in range(1,num_parts)]):
                    sum_invalid_ids += num
                    break

print(sum_invalid_ids)