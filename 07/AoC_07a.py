# Advent of Code 2024 - Day 7, 1st Challenge 
# Solution written by: Ioannis Doganos / 09-12-2024
# Strategy: Make all the combinations until a match is found. 

import time
start_time = time.time()

import re
import itertools

regex_numbers = r'^(\d+)\:\s((\d+\s?)+)\n*$'
d = {}
with open("./Input07.txt") as file:
    lines = file.readlines()
    for line in lines:
        result = re.search(regex_numbers, line)
        value_equation = int(result.group(1))
        numbers_string = result.group(2)
        numbers_list = re.findall(r'\d+', numbers_string)
        d[value_equation] = numbers_list
file.close()

def create_combinations(numbers, value):
    global count

    operators = ['+', '*']

    num_operations = len(numbers) - 1
    
    # Generate all possible operator combinations
    operator_combinations = itertools.product(operators, repeat=num_operations)
    
    results = []
    
    # For each combination of operators, build the expression
    for ops in operator_combinations:
        expression = numbers[0]  # Start with the first number
        for i, op in enumerate(ops):
            expression = eval(str(expression) + op + numbers[i+1]) # Do the maths from left to right
        if expression == value: 
            count += value
            break
                
    return results

# -- Main --
count = 0
for value, list_of_numbers in d.items():
    combinations = []
    if len(list_of_numbers) == 1:
        if value == int(list_of_numbers[0]):
            count += value
            continue
    elif len(list_of_numbers) == 0:
        continue
    else:
        combinations = create_combinations(list_of_numbers, value)        

if __name__ == "__main__":
    print(count)

    print("--- %s seconds ---" % (time.time() - start_time))
