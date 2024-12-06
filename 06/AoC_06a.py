# Advent of Code 2024 - Day 6, 1st Challenge 
# Solution written by: Ioannis Doganos / 06-12-2024
# Strategy: Replicate the steps of the guard. Create a matrix and rotate it so that the guard always "looks" on the right. More explanations are given at the comments of the code.

import numpy as np # Used to create an array that will be rotated.

# Class and function to find the starting position of the guard.
class myarray(np.ndarray):
    def __new__(cls, *args, **kwargs):
        return np.array(*args, **kwargs).view(myarray)
    def index(self, value):
        return np.where(self == value)

def find_position(matrix):
    a = myarray(matrix)
    index = a.index(">")

    row_position = index[0][0]
    column_position = index[1][0]

    return row_position, column_position


with open("./Input06.txt") as file:
    lines = file.readlines()
file.close()

list_characters = []
for line in lines:
    list_characters.append(list(line.strip()))

list_characters
matrix = np.array(list_characters)

# Start by rotating the matrix so that the guard will head right. 
for i, orientation in enumerate(['v', '<', '^']):
    if np.any(matrix == orientation):
        matrix[matrix == orientation] = '>'
        matrix = np.rot90(matrix, k=i+1)
        break

row_position, column_position = find_position(matrix)


def count_path():
    global count, matrix, found, column_position, row_position
    found = False 
    for i in range(column_position + 1, len(matrix[row_position])): # Searching the positions on the right of the guard.
        value = matrix[row_position][i]
        if value == '.':
            count += 1
            matrix[row_position][i] = 'X'
        elif value == 'X':
            pass
        else:
            found = True
            matrix[row_position][i-1] = '>'
            matrix[row_position, column_position] = 'X'
            break


count = 0
found = True
while found: # Continue until no obstacle is found on the right of the guard.
    count_path()

    # Rotate the matrix and find the new starting position.
    matrix = np.rot90(matrix, k=1) 
    row_position, column_position = find_position(matrix)

print(count+1) # +1 Because is the starting position of the last "walk" that has not been counted as a visited place. 
