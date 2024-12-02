# Advent of Code 2024 - Day 2, 2nd Challenge 
# Solution written by: Ioannis Doganos / 02-12-2024
# Strategy: In each list, remove one element and check if it complies with the requirements, with the same way the first challenge is solved.

from Aoc_02a import list_total, check_if_acceptable, convert_to_number

# --Main--
count_b = 0
for list_of_list in list_total:
    for x in range(len(list_of_list)): # Iterate through the list
        new_lists = [v for i, v in enumerate(list_of_list) if i != x] # Remove the element in position x of the list
        list_ = convert_to_number(new_lists)
        accepted = check_if_acceptable(list_)
        if accepted:
            count_b += 1
            break # If acceptable, do not continue

print(count_b)