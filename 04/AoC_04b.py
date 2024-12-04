# Advent of Code 2024 - Day 4, 1st Challenge 
# Solution written by: Ioannis Doganos / 04-12-2024
# Strategy: "Create" 3x3 lists and iterate their main diagonals. Put all the results in a string (common to the 1st challenge strategy).

from AoC_04a import list_characters

# Extract the string of the diagonals of the 3x3 lists.
def list_3x3_iterate(list_, final_string):
    positions_3x3 = [0,1,2]
    for i,k in zip(positions_3x3, positions_3x3[::-1]):
        final_string += ''.join(list_[i][k])
    for i in positions_3x3:
        final_string += ''.join(list_[i][i])

    final_string += '-'
    return final_string

final_string = ''
# Create the 3x3 lists by iterating the file.
for i in range(len(list_characters)-2):
    for k in range(len(list_characters[i])-2):
        list_to_parse = [
            list_characters[i][k:k+3],
            list_characters[i+1][k:k+3],
            list_characters[i+2][k:k+3]
        ]
        final_string = list_3x3_iterate(list_to_parse, final_string)

count = 0
for word in ['MASMAS', 'MASSAM', 'SAMSAM', 'SAMMAS']:
    count += final_string.count(word)
    
print(count)
