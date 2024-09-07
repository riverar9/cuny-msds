def answer_printer(question_number:int, value):
    question_number_print = f'   {question_number}'[-3:]
    print(f'Question{question_number_print}:\t{value}')

# 1. Create a variable y and set it to 5

y = 5
answer_printer(1, y)

# 2. Create a string variable called first_name and set it to your first name.

first_name = 'Richie'
answer_printer(2, first_name)

# 3. Create a string variable called last_name and set it to your last name.

last_name = 'Rivera'
answer_printer(3, last_name)

# 4. Create a string variable called full_name and set it equal to your full name using variables above.

full_name = first_name + ' ' + last_name
answer_printer(4, full_name)

# 5. Assign 20 to the variable hours_worked, 15 to the variable wage_per_hour and the product of the two to variable total_pay 

hours_worked = 20

wage_per_hour = 15

total_pay = hours_worked * wage_per_hour

answer_printer(5, total_pay)

# 6. Create a variable called x and set it to 10. Then create a variable y that equals to x to the 7th power 

x = 10
y = x ** 7
answer_printer(6, y)