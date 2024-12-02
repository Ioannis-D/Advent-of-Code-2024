# Advent of Code 2024 - Day 2, 1st Challenge 
# Solution written by: Ioannis Doganos / 02-12-2024
# Strategy: First, read the file and insert each number to a list (having a list of list). Then, iterate through the list of lists and count the ones that comply with the requirements.

def read_input(file_name):
    list_total = []
    with open(file_name) as file:
        for line in file:
            list_total.append(line.rstrip().split(" "))
    file.close()

    return list_total

def convert_to_number(list_of_list): # Convert each element of each list to number (to be able to correctly check the substraction)
    list_ = list(map(int,list_of_list))

    return list_

def check_if_acceptable(list_): 
    acceptable = False # Initiate the variable
    sorted_ = all((list_[i] - list_[i+1] >= 1 and list_[i] - list_[i+1] <= 3 ) for i in range(len(list_) - 1)) # Check if the list is sorted by ascending order and also the difference between consecutive numbers is between 1 and 3.
    if sorted_ : 
        acceptable = True
    else: 
        sorted_ = all((list_[i] - list_[i+1] <= -1 and list_[i] - list_[i+1] >= -3 ) for i in range(len(list_) - 1)) # The same but for descending order.
        if sorted_: acceptable = True
    
    return acceptable

def count_acceptable(list_total): # Count the "aceptable" lists
    count = 0
    for list_of_list in list_total:
        list_ = convert_to_number(list_of_list)
        acceptable = check_if_acceptable(list_)
        if acceptable: count += 1

    return count


# -- Main --
list_total = read_input("./Input02.txt") #-> Is a list of lists

count_a = count_acceptable(list_total)

if __name__ == "__main__":
    print(count_a)
