# 1. Create a list called animals that contain the following: cat, dog, manta ray, horse, crouching tiger
animals = [
    'cat',
    'dog',
    'manta ray',
    'horse',
    'crouching tiger'
]

# 2. Repeat question 1 and loop through and print each item in the animal list by iterating through an index number and using range(). Set a variable len_animals to the length of the animal list.

for index in range(0,len(animals)):
    print(animals[index])

# 3. Programmatically reorganize the countdown list below in descending order and return the value of the 5th element in the sorted countdown list.
#     The 5th element will be stored in the variable the_fifth_element, which currently below has a dummy value of -999.
#     Remember, the index number of the 5th element is not 5
countdown = [9, 8, 7, 5, 4, 2, 1, 6, 10, 3, 0, -5]
the_fifth_element = -999

descending_countdown = []

# To do this we'll iterate through "countdown" once.
# If we're on the first element, then it's automatically added and we continue onward
# If it isn't the first element, then we will insert the item in the correct space by reviewing the entries in the "descending_countdown" list.
for countdown_index in range(0, len(countdown)):
    countdown_item = countdown[countdown_index]
    
    if countdown_index == 0:
        descending_countdown.append(countdown_item)
    
    else:
        for desc_index in range(0, len(descending_countdown)):
            desc_item = descending_countdown[desc_index]
            
            if countdown_item >= desc_item:
                descending_countdown.insert(desc_index, countdown_item)
                break
            
            if desc_index == len(descending_countdown)-1:
                descending_countdown.append(countdown_item)

print(descending_countdown[4])

# 4. Write a program to add item 7000 after 6000 in the following Python List
list1 = [
    10,
    20,
    [
        300,
        400,
        [
            5000,
            6000
        ],
        500
    ],
    30,
    40
]

list1[2][2].append(7000)

print(list1)

# #Expected output:
# #[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

# 5. Write a program to remove all occurrences of item 20 in the following list.
list2 = [5, 20, 30, 15, 20, 30, 20]

def remove_values_from_list(remove_item, cleanup_list:list):
    # initialize an empty list
    return_list = []
    
    # Iterate through each item in the "cleanup_list" and append the item to "return_list" if it does not equal "remove_item"
    for element in cleanup_list:
        if element != remove_item:
            return_list.append(element)
    
    return return_list

print(
    remove_values_from_list(
        20,
        list2
    )
)

# 6. Using the following dictionary .. (Use python to solve for the answer.)
dict = {"Course": "DATA 606", "Program": "MSDS", "School": "CUNYSPS"}

# a. What is the name of the course?
print(f"The name of this course is '{dict['Course']}'.")

# b. Change the course to DATA602
dict['Course'] = 'DATA602'
print(f"The new name of this course is '{dict['Course']}'.")

# c. Add new information to the dictionary - "Professor" with "Schettini"
dict['Professor'] = 'Schettini'
print(f"The key 'Professor' has been added with the value '{dict['Professor']}'.")

# d. Using the len function, find how many keys there are in the dictionary. 
print(f"There are {len(dict.keys())} keys in 'dict'.")


# 7.  Write a Python program to change Brad’s salary to 7500 in the following dictionary.
sample_dict = {
    'emp1': {'name': 'Amanda', 'salary': 8200},
    'emp2': {'name': 'John', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 700}
}

sample_dict['emp3']['salary'] = 7500