# Advent of Code 2024 - Day 3, 2nd Challenge 
# Solution written by: Ioannis Doganos / 03-12-2024
# Strategy: Delete the text between don't() and do() and repeat the process of the first challenge. If there is no do() after the don't() until the end of the file, remove it also (this is the reason extra lines are removed when the file is read).

from AoC_03a import *

#Replace whatever between the don't() and the first occurance of do() or the end of the file with nothing.
regex_replace = r"don't\(\).+?(do\(\)|$)" 
line = re.sub(regex_replace, '', line)

# Use the same process as in the first challenge.
count = matches(line, regex_pattern, regex_groups)  

print(count)