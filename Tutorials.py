
                                        # Hello world

#print("Hello world")

#                              _______________________________________

                                       #Drawing shape

#Right Triangle

    #print("   /|")
    #print("  / |")
    #print(" /  |")
    #print("/___|")

#                              _______________________________________

                                  #Variables & Data types

#characterAge = "70"
#CharacterAge = 70                       #This is an int/ float/ anytype of number

#isMale = False # Boolean value
#print("There once was a man named " + characterName +  ", ") #Adds in the name of the character with the +
#print("he was " + characterAge + " years old. ")

#characterName = "Mike"                 # Change or update the variable
#print("He really liked the name " + characterName+ ", ")
#print("but didn't like being " +characterAge+".")

#                              _______________________________________

                                         # Strings

#phrase = "Girafee Academy"

#print (phrase + " is cool")             # concatination
#print("Giraffee\nAcademy")              # n is new like
#print("Giraffe\"Academy")               # print qoutation mark

#                              _______________________________________

                                          #functions
#phrasee = "Girafee"

# lowercase ( can also do for upper case )

    #print (phrasee.lower())             # make the statement lower case

# Asks if its uppercase ( can also do this for lower case )

    #print(phrasee.isupper())            # is it upper case

# Combining the first two together

    #print(phrasee.upper().isupper())    #using one function after the next

#Tell you how long the whole string is

    #print(len(phrasee))                 #length function - how long is it

#Tells you the letter of the number you put in

    #print(phrasee[0])                   # prints whichever index you want
    #print(phrasee[3])

#tells you which number colrelates to the letter inserted

    #print(phrasee.index("G"))

#Tells you where the phrase begins

    #print (phrasee.index("afee"))

#replacing - Can do this with words or letters

    #print(phrasee.replace("Girafee", "Hedghog")) # Replaces the word you put in with the word you put next

#                              _______________________________________

                                            #Numbers

#print number - no issue with any type of number

    #print(5)
    #print (2.3)
    #print (-4.2)

#basic math

    #print ( 5+2)
    #print(5*4)
    #print(7*3+2)
    #print(7*(3+2))          # follows order of operation
    #print (10%3)            #remainder

#myNumber = 5

#print(myNumber)         # prints out the number assigned

#Turning number to string

    #print(str(myNumber))

#myNum = -7

#Absolute value of number

    #print(abs(myNum))

# Power

    #print(pow(3,2))

# math function

    #print(max(4,6)) # which has the heightest value
    #print(min(4,6)) # which has the lowest value
    #print(round(3.2)) # rounds it based on the decimal

#from math import * # importing

    #print(floor(3.7)) # rounds down no matter what
    #print(ceil(3.7)) # rounds up no matter what
    #print(sqrt(36)) #square root

#                              _______________________________________

                                         # input

# allow user to input information and store it in a variable

    #name = input(" Enter your name: ") #this sets variable equal to the input
    #age = input( "Enter your age: ")
    #print("Hello "+name+ "! You are "+age+ " years old")

#                              _______________________________________

                                         # Lists
# First we give it a name

    #Friends = ["Kevin", "Karen", "Jim"]

    #print(Friends[2])
    #print(Friends[1:])
    #print(Friends[0:2])

    #Friends[1] = "Mike"
    #print(Friends[1])
#                              _______________________________________

                                         # List function

#lucky_numbers = [4,8,15,16.23,42]
#friends = ["Kevin","Karen","Jim","Jim", "Oscar", "Toby"]

#Extend function

    #friends.extend(lucky_numbers)
    #print(friends)

#append

    #friends.append("creed")
    #print(friends)

#Insert

    #friends.insert(1,"Kelly")

#remove

    #friends.remove("creed")
    #print(friends)

#friends.clear()

    #print(friends)

#pop function

    #friends.pop()
    #print(friends)

#index function

    #print(friends.index("Kevin"))

#Count function

#print(friends.count("Jim"))

#Sort function

#friends.sort()
#print(friends)

#copy function

#friends2=friends.copy()
#print(friends2)

#                              _______________________________________

                                         # Tuples

#coordinates = (4,5) # This is how you create a tuple, and inside them you want to put your numbers

#Tuples are immutable meaning they cant be changed or modified. Once it is created you can't change it, modify it
# add elements to it or erase elements from it

#print(coordinates[0]) #This is the way to access the tuple, Since tuples are indexes 4 is at space 0 and 5 is at space one

#Difference between tuples and lists: A list you can assign different variables and change the index while in a tuple you cannot

#coordinates = [(4, 5),(6, 7),(8, 9)] #this list cannot be changed due to the tupples

#                              _______________________________________

                                         # Functions

#for functions we must use a keyword in python called def

#def sayhi(name): #This shows python that the user wants to use a function
   # print("Hello user!")

#sayhi()

#def sayhi(name,age): #we can have as many parameters as we want inside a function
    #print("Hello" + name + "you are " + age)
#sayhi(" Anya", "21")
#sayhi(" Litobug <3", "20")

#                              _______________________________________

                                         # Return statements
#def cube(num):
    #return(num*num*num)
#print(cube(3))

#                              _______________________________________

                                         # If statements
#is_male = False

#if is_male:
    #print("Cool you're a dude")
#else:
   #print("You ain't a dude")

#                              _______________________________________

                                         # If statements and comparison
#def max_num(num1,num2,num3):
    #if num1 >= num2 and num1 >= num3:
        #return num1
    #elif num2>=num1 and num2>=num3:
        #return num2
    #else:
        #return num3
#print(max_num(3,4,5))

#                              _______________________________________

                                         #Dictionaries

#monthConversion = {
   # "Jan": "January",
    #"Feb": "February",
   # "Mar": "March",
   # "Apr": "April",
   # "May": "May",
   # "Jun": "June",
   # "Jul": "July",
   # "Aug": "August",
   # "Sep": "September",
   # "Oct": "October",
   # "Nov": "November",
   # "Dec": "December",
#}

#print(monthConversion["Nov"])
#print(monthConversion.get("Dec", "Not a valid key"))
#print(monthConversion.get("asdfg", "Not a valid key"))
#                              _______________________________________

                                         #While loops
#i = 1

#while i <=10:
#    print(i)
#    i = i+1
#print("Done with the loop")

#                              _______________________________________

                                         #For loops
#friends = ["Jim", "Dude", "not dude"]
#for friend in friends:
 #   print(friend)

#for index in range(10):
 #   print(index)

#                              _______________________________________

                                         #Exponent Function
#def raise_to_power(basenumber, pow_number):
 #   result = 1
  #  for index in range(pow_number):
   #     result = result*basenumber
    #return result

#print(raise_to_power(3,2))
#                              _______________________________________

                                         #2D litss and Nested loops
# number_grid =[
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
#     ]
# print(number_grid[0][0])
#
# for row in number_grid: # we see them are horizontal rows, for each of them we are going to loop through
#     print(row)
#     #for column in row: # this will give us each individual element inside number grid
#         #print(column)
                                    # Try Except
# try:
#     number = int(input("Enter a number: "))  # if the user does not enter an int it will cause issues
#     print(number)
# except ZeroDivisionError as err:  # Except specific types
#     print(err)
# except ValueError:
#     print("Invalid input")

                                        # Reading Files

employee_file = open("employees.txt", "r")  # The file is going to be read
print(employee_file.read())
print(employee_file.readline())

employee_file.close()






