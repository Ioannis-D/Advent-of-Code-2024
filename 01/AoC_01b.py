# Advent of Code 2024 - Day 1, 2nd Challenge 
# Solution written by: Ioannis Doganos / 01-12-2024
# Strategy: Count the number of times each number appears to each column. Then multiply the number of times the values from the first list appear in the second list, multiplied by the number and the times it appears in the first list.

from AoC_01a import list_first_numbers, list_second_numbers
from collections import Counter # To count the time each value appears in each list. Creates a dictionary,

dict_first_numbers = Counter(list_first_numbers)
dict_second_numbers = Counter(list_second_numbers) 

# Initialize the sum value.
sum = 0
for number, times in dict_first_numbers.items():
    sum += dict_second_numbers[number] * number * times
print(sum)
