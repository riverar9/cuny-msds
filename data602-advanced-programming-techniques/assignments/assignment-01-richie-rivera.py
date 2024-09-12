#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95
 
# Get the test scores.
test1 = int(input('Enter the score for test 1:\n\t')) # RR: Converted this into an integer
test2 = int(input('Enter the score for test 2:\n\t')) # RR: Converted this into an integer
test3 = int(input('Enter the score for test 3:\n\t')) # RR: This line was missing in the collection of test Scores. Converted this into an integer
# Calculate the average test score.
average = (test1 + test2 + test3) / 3 # RR: Added the brackets to perform the sum operation before the division operation.
# Print the average.
print(f'The average score is {average}') # RR: Changed this line to be more readable
# If the average is a high score,
# congratulate the user.
if average >= HIGH_SCORE: # RR: Updated variable name to reflect the previous high hscore
    print('Congratulations!')
print('That is a great average!')

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for 
# the length and width of two rectangles and prints to the user the area of both rectangles. 

def get_rectangular_area(length, width):
    return length * width

def input_int(input_text):
    response = int(input(input_text + '\n\t'))

    if type(response) == int:
        return response
    else:
        print('That was not a valid response. Please, try again.')
        return input_int(input_text)

def get_user_rectangle_input_and_area(rectangle_id):
    length = input_int(f"What is rectangle {rectangle_id}'s length?")
    width = input_int(f"What is rectangle  {rectangle_id}'s width?")

    print(f"Rectangle {rectangle_id}'s area is : {length * width}")

for each_number in range(0,2):
    get_user_rectangle_input_and_area(each_number)

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.

name = input('What is your name?\n\t')
age = input_int('What is your age?\n\t')

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

print(f"Happy Birthday {name}! You are {age} years old today!")