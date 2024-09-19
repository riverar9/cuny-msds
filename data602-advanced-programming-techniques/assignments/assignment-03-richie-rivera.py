# %%
def q1():
# Q1: Write a program that prompts the user for a meal: breakfast, lunch, or dinner. Then using if statements and else statements print the user a message recommending a meal. For example, if the meal was breakfast, you could say something like, “How about some bacon and eggs?”
# The user may enter something else in, but you only have to respond to breakfast, lunch, or dinner.
    valid_input = ['a','b','c','breakfast','lunch','dinner']
    
    responses = [
        'Hope you like fluffy pancakes!',
        'Did you know that in France they call it le dejeuner?',
        'Ever have sleep for dinner?'
    ]

    response_dictionary = {}
    count = 0
    for each_input in valid_input:
        response_dictionary[each_input] = responses[count % 3]
        count += 1

    response_validated = False

    while not response_validated:
        selected_meal = input('What meal you like to eat?\n\tA. Breakfast\n\tB. Lunch\n\tC. Dinner\n\n')
        if selected_meal.lower() in valid_input:
            print(response_dictionary[selected_meal])
            response_validated = True
        else:
            print("I'm not sure what meal that is? Can you either type the letter or the meal?")

def q2(hours_worked, rate_of_pay):
# Q2: The mailroom has asked you to design a simple payroll program that calculates a student employee’s gross pay, including any overtime wages. If any employee works over 20 hours in a week, the mailroom pays them 1.5 times their regular hourly pay rate for all hours over 20. 
# You should take in the user’s input for the number of hours worked, and their rate of pay.
    base_pay = min(hours_worked, 20) * rate_of_pay

    if hours_worked > 20:
        overtime_pay =  1.5 * (hours_worked - 20) * rate_of_pay
    

    print(f"""
    This student worked {hours_worked} hours at a base rate of ${rate_of_pay} an hour. 
    They should be paid a total of ${base_pay + overtime_pay:,} where ${base_pay:,} is for their regular rate and ${overtime_pay:,} for their overtime rate.
    """)
    

def q3_time_ten(number):
# Q3: Write a function named times_ten. The function should accept an argument and display the product of its argument multiplied times 10.
    print(f"{number} times 10 is {10*number}")

def q4_main():
# SQ4: Find the errors, debug the program, and then execute to show the output.
    calories1 = float(input( "How many calories are in the first food?"))
    calories2 = float(input( "How many calories are in the first food?"))
    showCalories(calories1, calories2)

def showCalories(calories1, calories2):
   print("The total calories you ate today: {:.2f}".format(calories1 + calories2))

def q5():
# Q5: Write a program that uses any loop (while or for) that calculates the total of the following series of numbers:
#          1/30 + 2/29 + 3/28 ............. + 30/1
    running_total = 0
    for each_number in range(0,30):
        running_total += (each_number + 1) / (30 - each_number)

    print(f"The total of this sum of fractions is: {running_total}")
        

def q6(triangle_base, triangle_height):
# Q6: Write a function that computes the area of a triangle given its base and height.
# The formula for an area of a triangle is:
# AREA = 1/2 * BASE * HEIGHT

# For example, if the base was 5 and the height was 4, the area would be 10.
# triangle_area(5, 4)   # should print 10
    print(f"The area of the triange with a base of {triangle_base} and a height of {triangle_height} is {0.5 * triangle_base * triangle_height}")

# %%
def main():
    q1()
    q2(40, 80)
    q3_time_ten(5)
    q4_main()
    q5()
    q6(4,4)

# %%
if __name__ == '__main__':
    main()