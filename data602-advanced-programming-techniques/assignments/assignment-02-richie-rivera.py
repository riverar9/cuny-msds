# %%
def q1():
    print("""
          Q1. What will the following code display?
                The code below will print an empty list.
                    numbers = [1, 2, 3, 4, 5]
                    print(numbers[1:-5])
          
          Can you debug and fix the output? The code should return the entire list
                
                One way to fix it we'll need to change it to:
                    numbers = [1, 2, 3, 4, 5]
                    print(numbers[0:])

                or we can simply do the below as we want to print the entire list.:
                    print(numbers)
    """)


# %%
def q2():
# Q2. Design a program that asks the user to enter a store’s sales for each day of the
# week. The amounts should be stored in a list. Use a loop to calculate the total sales for
# the week and display the result.
    week_days = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
    ]

    weekly_sales = []

    for week_day in week_days:
        weekly_sales.append(int(input(f"What are the sales for {week_day}?\n\t")))

    total_sales = 0

    for daily_sales in weekly_sales:
        total_sales += daily_sales
    
    return total_sales

# %%
def q3():
# Q3. Create a list with at least 5 places you’d like to travel to. Make sure the list isn’t in
# alphabetical order
# ● Print your list in its original order.
# ● Use the sort() function to arrange your list in order and reprint your list.
# ● Use the sort(reverse=True) and reprint your list.
    travel_wishes = [
        'Berlin',
        'Prague',
        'Taipei',
        'Tokyo',
        'Kigali',
        'Fez',
        'Santiago',
        'Lima',
    ]

    print(travel_wishes)

    travel_wishes.sort()
    
    print(travel_wishes)

    travel_wishes.sort(reverse=True)

    print(travel_wishes)

    pass

# %%
def q4():
# Q4. Write a program that creates a dictionary containing course numbers and the room
# numbers of the rooms where the courses meet. The program should also create a
# dictionary containing course numbers and the names of the instructors that teach each
# course. After that, the program should let the user enter a course number, then it should
# display the course’s room number, instructor, and meeting time.
    course_rooms = {
        'DATA602' : 'Room 001',
        'DATA624' : 'Room 025'
    }

    course_instructors = {
        'DATA602' : 'Nicholas Schettini',
        'DATA624' : 'Jeff Nieman'
    }

    course_meet_times = {
        'DATA602' : 'Thursday from 1700 - 1800',
        'DATA624' : 'Tuesday from 1900 - 2000'
    }

    valid_inputs = '\n\t'.join(
        list(
            set(
                list(course_rooms.keys()) +
                list(course_instructors.keys()) +
                list(course_meet_times.keys())
            )
        )
    )

    valid_response = False

    while not valid_response:
        selected_course = input(f'Input your course number. Valid inputs are:\n\t{valid_inputs}').upper()

        if selected_course in valid_inputs:
            valid_response = True
        else:
            print(f"'{selected_course}' was not a valid response. Please try again or press CTRL+C to exit.")
    
    print(f"""
        For the selected course "{selected_course}":
            Instructor:     {course_instructors[selected_course]}
            Meeting Room:   {course_rooms[selected_course]}
            Meet Time:      {course_meet_times[selected_course]}
    """)
# %%
def lookup_email(email_dict):
    lookup_name = input("What is the name of the person you want to lookup?\n\t")
    if lookup_name in email_dict.keys():
        print(email_dict[lookup_name])
    else:
        print(f"{lookup_name} doesn't exist in the dictionary!")

def add_modidfy_email(email_dict, add_operation = True):
    if add_operation:
        new_name = input("What is the name of the person you want to add?")
        new_email = input(f"What is {new_name}'s email address?")
    else:
        new_name = input("What is the name of the person you want to modify?")
        new_email = input(f"What is {new_name}'s new email address?")

    email_dict[new_name] = new_email
    
    print(f"{new_name}'s email {new_email} has been added successfully!")
    return email_dict

def delete_email(email_dict):
    delete_name = input('What is the name of the person you want to delete?')

    if delete_name not in email_dict.keys():
        print(f"{delete_name} was not found!")
        return email_dict
    else:
        del email_dict[delete_name]
        print(f"{delete_name}'s email address was successfully deleted.")
        return email_dict


def q5():
# Q5. Write a program that keeps names and email addresses in a dictionary as
# key-value pairs. The program should then demonstrate the four options:
# ● look up a person’s email address,
# ● add a new name and email address,
# ● change an existing email address, and
# ● delete an existing name and email address.
    emails = {
        "Richie Rivera" : "richie.rivera89@cuny.spsmail.cuny.edu"
    }

    root_valid_options = [
        1,
        2,
        3,
        4
    ]

    root_valid_response = False

    while not root_valid_response:
        root_selection = int(
            input("""
            Please select an option:
                1 - lookup an existing person's email address
                2 - add a new name and email address
                3 - change an existing person's email address
                4 - Delete an existing name and email address
            """)
        )

        if root_selection in root_valid_options:
            root_valid_response = True
        else:
            print(f"'{root_selection}' was not a valid response. Please try again or press CTRL+C to exit.")
    
    if root_selection == 1:
        lookup_email(emails)
    elif root_selection == 2:
        emails = add_modidfy_email(emails)
    elif root_selection == 3:
        emails = add_modidfy_email(emails, add_operation=False)
    elif root_selection == 4:
        emails = delete_email(emails)
    
    print(emails)

# %%
def main():
    q1()
    q2()
    q3()
    q4()
    q5()