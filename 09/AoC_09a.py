# Advent of Code 2024 - Day 9, 1st Challenge 
# Solution written by: Ioannis Doganos / 09-12-2024
# Strategy: Unfortunatelly, due to lack of time for creating a better solution, the strategy is: brute force. I will check other solutions for ideas, but the script uploaded will not be changed (except if necessary for 2nd challenge).
#           Make a list of each number and '.'. Extract the indeces of the '.' and replace them with the last numbers of the list created before. Finally, multiply each number left in the list with its index and return the result.

import time
start_time = time.time()

import re

with open("./Input09.txt") as file:
    string = file.readline() # The file is just one line
file.close()

# Create the list of numbers and '.'
list_numbers = []
for i in range(0, len(string)):
    if i%2 == 0: 
        for k in range(1, int(string[i]) +1):
            list_numbers.append(i//2)
    else:
        for k in range(0, int(string[i])):
            list_numbers.append('.')

# The indeces of the '.'
indices = [i for i, x in enumerate(list_numbers) if x == "."]

# Replace the first '.' with the last numbers of the list.
while indices:
    indice = indices[0]
    while True:
        if list_numbers[-1] != '.':
            list_numbers[indice] = list_numbers[-1]
            list_numbers = list_numbers[:-1]
            indices = [i for i, x in enumerate(list_numbers) if x == "."]
            break
        else:
            list_numbers = list_numbers[:-1]
            indices = [i for i, x in enumerate(list_numbers) if x == "."]

count = 0
for i in range(len(list_numbers)): 
    count += list_numbers[i] * i

if __name__ == '__main__':
    print(count)

    print("--- %s seconds ---" % (time.time() - start_time))
