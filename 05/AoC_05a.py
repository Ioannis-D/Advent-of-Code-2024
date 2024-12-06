# Advent of Code 2024 - Day 5, 1st Challenge 
# Solution written by: Ioannis Doganos / 05-12-2024
# Strategy: Unfortunately, this is a bit of a brute force: Create a dictionary with keys as the numbers included in the text to be printed, and values the list of numbers that have to be after them. Then, iterate each list from the end and check if the condition is met. Save the "good" and the "bad" lists, find the medium place of each "good" list and sum them. 

import time
start_time = time.time()

import pandas as pd
import re

rules = pd.read_csv("./Input05a.txt", sep="|", header=0, names=['Before', 'After'])

with open("./Input05b.txt") as file:
    lines = file.readlines()
file.close()

regeex_numbers = r'\d+'
new_list = []
for line in lines:
    new_list.append([int(x) for x in re.findall(regeex_numbers, line)]) 

keys_rules = set()
for x in new_list: 
    keys_rules = keys_rules.union(set(x))

d = {}
for i in keys_rules:
    d[i] = list(x for x in rules[rules['Before'] == i]['After'])

good_list = []
bad_list = []
for list_ in new_list:
    found = False
    stop = False
    for i in range(len(list_)-1, 0, -1):
        if not stop:
            for x in list_[0:i]:
                if x in d[list_[i]]:
                    found = True
                    bad_list.append(list_)
                    stop = True
                    break
    if not found:
        good_list.append(list_)

count = 0
for list_ in good_list:
    medium_position = int((len(list_)) / 2)
    count += list_[medium_position]

if __name__ == "__main__":
    print(count)

print("--- %s seconds ---" % (time.time() - start_time))
