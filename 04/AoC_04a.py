# Advent of Code 2024 - Day 4, 1st Challenge 
# Solution written by: Ioannis Doganos / 04-12-2024
# Strategy: Create a string of all the rows, columns and diagonals. Then, count the times the word XMAS or its reverse appears in the string.

import numpy as np

word = 'XMAS'
word_reverse = word[::-1]

with open("./input04.txt") as file:
    lines = file.read().splitlines()
file.close()

def find_diagonals(a): #Taken from https://stackoverflow.com/a/6313414
    diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]

    diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))

    diagonals = [n.tolist() for n in diags]

    return diagonals


# Create a list of characters for being easier to do the string of the diagonals.
list_characters = []
for line in lines:
    list_characters.append(list(line.strip()))

# Create a numpy matrix to be able to do the diagonals.
matrix = np.array(list_characters)

diagonals = find_diagonals(matrix)

list_diagonal = []
for diagonal in diagonals:
    list_diagonal.append(''.join(x for x in diagonal))
list_diagonal

list_vertical = []
transposed_list = list(list(x) for x in zip(*lines))
for lista in transposed_list:
    list_vertical.append(''.join(x for x in lista))
list_vertical

# Create a final string which contains all the rows, columns and diagonals.
full_string = '-'.join(x for x in lines)
full_string += '-'.join(x for x in list_diagonal)
full_string += '-'.join(x for x in list_vertical)

count = full_string.count(word) + full_string.count(word_reverse)

if __name__ == "__main__":
    print(count)
