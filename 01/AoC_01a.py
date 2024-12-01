# Advent of Code 2024 - Day 1, 1st Challenge 
# Solution written by: Ioannis Doganos / 01-12-2024
# Strategy: Regex was used to extract the numbers of the two columns. Then each column was assigned to a list which was sorted. Finally, the substraction and the sum of the elements took place.

import re

# Read the file (downloaded from Advent of Code and pasted to a .csv file).
with open("./Input01.csv") as file:
    list_first_numbers, list_second_numbers = [], [] # Create two empty lists to store the numbers.
    regex_grouping = r'(\d+)(\s+)(\d+)' 
    # Find the numbers and append them to the corresponding list.
    for row in file:
        result = re.search(regex_grouping, row)
        first_number = result.group(1)
        second_number = result.group(3)
        list_first_numbers.append(int(first_number)) # Convert the string to number.
        list_second_numbers.append(int(second_number))
    
# Close the file.
file.close()

# Sort the lists in ascending order. 
list_first_numbers.sort()
list_second_numbers.sort()

# Print the result by adding the absolute difference of the values of each list.
# Firstly, the two lists are combined with the zip to be able to retrieve each respective element.
# Then, the substraction takes place but with the absolute value. Finally, the results are sumed and the answer is revealed.
if __name__ == "main":
    print(sum(abs(x-y) for x, y in zip(list_first_numbers, list_second_numbers)))

