"""
This is going to take input from the user
and put it into a schedule (:
IF USER DID NOT DO THAT DATE, PRINT THAT THEY DID NOT COMPLETE THAT DAY
Put everything in a file, and open that file at the end to shower the user their
schedule for the whole week, IF the whole week is completed. 
"""

# CONSTANTS
WELCOME = "Welcome to"

# lists needed for each day
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]  # Days of the week
monday_schedule = []  # List for monday
tuesday_schedule = []  # List for tuesday
wednesday_schedule = []  # List for wednesday
thursday_schedule = []  # list for thursday
friday_schedule = []  # list for friday
saturday_schedule = []  # list for saturday
sunday_schedule = []  # list for sunday


def day_to_schedule():
    """
    In this function we are checking to see
    if the day is valid, and following up on that
    we are saying if they already did that specific day
    :return:
    """

    day_to_begin = input("What day would you like to schedule ? ")

    # This runs until the user inputs a proper date/ runs if user already finished a date
    while day_to_begin.lower() not in days:
        print("Sorry but I only know 7 days of the week, try again!\n"
              "You might have also already done that day!")
        day_to_begin = input("What day would you like to start with ? ")

    # Checks if the day is valid
    if day_to_begin.lower() in days:
        print("Great lets go to", day_to_begin)

        if day_to_begin.lower() == "monday":
            monday()

        elif day_to_begin.lower() == "tuesday":
            tuesday()

        elif day_to_begin.lower() == "wednesday":
            wednesday()

        elif day_to_begin.lower() == "thursday":
            thursday()

        elif day_to_begin.lower() == "friday":
            friday()

        elif day_to_begin.lower() == "saturday":
            saturday()

        else:
            sunday()


def monday():

    """
    This is Monday's function
    allowing the user to input for monday
    :return:
    """

    # MONDAY schedule
    print(WELCOME, "to Monday")
    print("Lets begin making your schedule:")
    # school_schedule = open('Schedule')

    monday_tasks = input("Insert the task you want to complete, STOP to stop: ")

    if monday_tasks == "STOP":  # If the user inputs STOP first, we assume they have no tasks
        monday_schedule.append("You have no tasks monday!")

    while monday_tasks != "STOP":
        monday_schedule.append(monday_tasks)
        monday_tasks = input("Insert the task you want to complete, STOP to stop: ")

    print("We are all done with Monday!")
    days.remove("monday")
    follow_up()
    # school_schedule.close()


def tuesday():

    """
    This is tuesdays function
    User inputs for tuesday
    :return:
    """

    print(WELCOME, "to Tuesday")
    print("Lets begin making your schedule:")
    # school_schedule = open('Schedule')

    tuesday_tasks = input("Insert the task you want to complete, STOP to stop: ")

    if tuesday_tasks == "STOP": # If the user inputs STOP first, we assume they have no tasks
        tuesday_schedule.append("You have no tasks Tuesday!")

    while tuesday_tasks != "STOP":
        tuesday_schedule.append(tuesday_tasks)
        tuesday_tasks = input("Insert the task you want to complete, STOP to stop: ")

    print("We are all done with Tuesday!")
    days.remove("tuesday")
    follow_up()

    # school_schedule.close()


def wednesday():

    """
    Wednesday function
    allows user to input for wendesday
    :return:
    """

    print(WELCOME, "to Wednesday")
    print("Lets begin making your schedule:")
    # school_schedule = open('Schedule')

    wednesday_tasks = input("Insert the task you want to complete, STOP to stop: ")

    if wednesday_tasks == "STOP": # If the user inputs STOP first, we assume they have no tasks
        wednesday_schedule.append("You have no tasks Wednesday!")

    while wednesday_tasks != "STOP":
        wednesday_schedule.append(wednesday_tasks)
        wednesday_tasks = input("Insert the task you want to complete, STOP to stop: ")

    print("We are all done with Wednesday!")
    days.remove("wednesday")
    follow_up()

    # school_schedule.close()


def thursday():

    """
    This is thursdays function
    Allows user to input for thursday
    :return:
    """

    print(WELCOME, "to Thursday")
    print("Lets begin making your schedule:")
    # school_schedule = open('Schedule')

    thursday_tasks = input("Insert the task you want to complete, STOP to stop: ")

    if thursday_tasks == "STOP": # If the user inputs STOP first, we assume they have no tasks
        thursday_schedule.append("You have no tasks Thursday!")

    while thursday_tasks != "STOP":
        thursday_schedule.append(thursday_tasks)
        thursday_tasks = input("Insert the task you want to complete, STOP to stop: ")

    print("We are all done with Thursday!")
    days.remove("thursday")
    follow_up()

    # school_schedule.close()


def friday():

    """
    This is fridays function
    Allows user to input for friday
    :return:
    """

    print(WELCOME, "to Friday")
    print("Lets begin making your schedule:")
    # school_schedule = open('Schedule')

    friday_tasks = input("Insert the task you want to complete, STOP to stop: ")

    if friday_tasks == "STOP": # If the user inputs STOP first, we assume they have no tasks
        friday_schedule.append("You have no tasks monday!")

    while friday_tasks != "STOP":
        friday_schedule.append(friday_tasks)
        friday_tasks = input("Insert the task you want to complete, STOP to stop: ")

    print("We are all done with Friday!")
    days.remove("friday")
    follow_up()

    # school_schedule.close()


def saturday():

    """
    This is saturdays function
    allows user to input for saturday
    :return:
    """

    print(WELCOME, "to Saturday")
    print("Lets begin making your schedule:")
    # school_schedule = open('Schedule')

    saturday_tasks = input("Insert the task you want to complete, STOP to stop: ")

    if saturday_tasks == "STOP": # If the user inputs STOP first, we assume they have no tasks
        saturday_schedule.append(" You have no tasks Saturday!")

    while saturday_tasks != "STOP":
        saturday_schedule.append(saturday_tasks)
        saturday_tasks = input("Insert the task you want to complete, STOP to stop: ")

    print("We are all done with Saturday!")
    days.remove("saturday")
    follow_up()

    # school_schedule.close()


def sunday():

    """
    This is sundays function
    Allows user to input for sunday
    :return:
    """

    print(WELCOME, "to Sunday")
    print("Lets begin making your schedule:")
    # school_schedule = open('Schedule')

    sunday_tasks = input("Insert the task you want to complete, STOP to stop: ")

    if sunday_tasks == "STOP": # If the user inputs STOP first, we assume they have no tasks
        sunday_schedule.append("You have no tasks Sunday!")

    while sunday_tasks != "STOP":
        sunday_schedule.append(sunday_tasks)
        sunday_tasks = input("Insert the task you want to complete, STOP to stop: ")

    print("We are all done with Sunday!")
    days.remove("sunday")
    follow_up()

    # school_schedule.close()


def follow_up():

    """
    This function allows user to decide if they want another day
    :return:
    """

    another_day = input("Would you like to do another day? ")

    if another_day.lower() == "yes" or another_day.lower() == "y":
        day_to_schedule()

    else:
        goodbye()


def goodbye():

    """
    This function prints out the schedule for the user
    :return:
    """

    print("Your tasks for this week are:")  # Print out the tasks
    print("Monday", monday_schedule)  # Monday
    print("Tuesday", tuesday_schedule)  # Tuesday
    print("Wednesday", wednesday_schedule)  # Wednesday
    print("Thursday", thursday_schedule)  # Thursday
    print("Friday", friday_schedule)  # Friday
    print("Saturday", saturday_schedule)  # Saturday
    print("Sunday", sunday_schedule)  # Sunday


if __name__ == '__main__':

    print("Welcome to schedule builder")
    day_to_schedule()
