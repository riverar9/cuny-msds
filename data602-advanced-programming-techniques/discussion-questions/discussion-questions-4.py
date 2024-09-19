# %%
# 1. Write a function to calculate the area and perimeter of a rectangle.
def get_rect_area(width, length):
    print(f"The area of this rectangle is {width*length}")

def get_rect_premiter(width, length):
    print(f"The area of this rectangle is {2*width + 2*length}")

def check_if_number(input):
    # Check if the input is a number
        try:
            input = float(input)
            return True
        except ValueError:
            return False

def get_number(input_text):
    valid_response = False
    
    while not valid_response:
        response = input(input_text)

        valid_response = check_if_number(response)

        if valid_response:
            return float(response)
        else:
            print("The input value of '{response}' is invalid. Please try again. \n{input_text}")

def q1():
    width = get_number("What is the rectangle's width?\n")
    length = get_number("What is the rectangle's length?\n")

    get_rect_area(width, length)
    get_rect_premiter(width, length)    

# 2. Write a function to check if a number is even or not.  The function should indicate to the user even or odd.
def q2(input_number = None):
    if input_number is None:
        input_number = get_number("What number do you want to check?\n")

    if input_number % 2 == 0:
        print('Your number is even!')
    else:
        print('Your number is odd!')
# 3. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample string: “CUNY sps”
    # of upper case characters: 4
    # of lower case characters: 3

def q3():
    input_string = input('What string do you want to check?\n')

    upper_count = 0
    lower_count = 0
    other_count = 0

    for letter in input_string:
        if letter.isupper():
            upper_count += 1
        elif letter.islower():
            lower_count += 1
        else:
            other_count += 1
    
    print(f'There are {upper_count} uppercase letters and {lower_count} lowercase letters. There are also {other_count} other character(s) in this string.')

# 4. Write a Python function to sum all the numbers in a list
def q4(input_list:list):
    not_numbers = []
    
    running_sum = 0

    for element in input_list:
        if check_if_number(element):
            running_sum += float(element)
        else:
            not_numbers.append(element)
    
    output_print = f"The total of this list is {running_sum}"
    
    if len(not_numbers) > 0:
        print_join = '\n\t'.join(not_numbers)
        output_print += f'\n    These items in the list are not numbers:\n\t{print_join}'
    
    print(output_print)


# 5. Create a function that shows an example of global vs local variables.
variable = 10

def q5():
    variable = 25
    print(f"Inside the function q5() the value of 'variable' is {variable}")

# 6. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
def q6(input_number):
    return lambda second_number: input_number*second_number

def main():
    q1()
    q2()
    q3()
    q4()
    print(f"Outside of the function q5() and before it runs, value of 'variable' is {variable}")
    q5()
    print(f"Outside of the function q5() and after it runs, value of 'variable' is {variable}")
    
    q6_first_num = 5
    q6_second_num = 10
    q6item = q6(q6_first_num)
    print(f"{q6_first_num} * {q6_second_num} = {q6item(q6_second_num)}")

# %%
if __name__ == '__main__':
    main()
