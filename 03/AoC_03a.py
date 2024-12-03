# Advent of Code 2024 - Day 3, 1st Challenge 
# Solution written by: Ioannis Doganos / 03-12-2024
# Strategy: Regex, of course!

import re

def read_input(file_name):
    with open(file_name) as file:
        line = file.read().replace("\n", "") # The replace has been added due to the second challenge
    file.close()

    return line

# Iterate through the matches found in the file and return the count of the multiplication of the two numbers.
def matches(input_, pattern, regex_groups, count=0):
    list_of_matches = re.findall(pattern, input_)
    for matches in list_of_matches:
        result = re.search(regex_groups, matches)
        number_1 = int(result.group(1))
        number_2 = int(result.group(2))
        count += number_1 * number_2

    return count

line = read_input("./Input03.txt")

regex_pattern = r'mul\(\d{1,3},\d{1,3}\)'
regex_groups = r'\((\d+),(\d+)\)$'
count = matches(line, regex_pattern, regex_groups)

if __name__ == "__main__":
    print(count)
