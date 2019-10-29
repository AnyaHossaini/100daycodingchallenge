"""
The ASCII converter takes text the user inputs and converts it into ASCII decimal numbers

"""


def convert(sentence):

    value_of_letter = 65
    conversion = " "
    for letters in sentence:
        if letters == "A":
            conversion = conversion + str(value_of_letter)
        if letters == "B":
            conversion = conversion + str(value_of_letter+1)
        if letters == "C":
            conversion = conversion + str(value_of_letter+2)
        if letters == "D":
            conversion = conversion + str(value_of_letter+3)
        if letters == "E":
            conversion = conversion + str(value_of_letter+4)
        if letters == "F":
            conversion = conversion + str(value_of_letter+5)
        if letters == "G":
            conversion = conversion + str(value_of_letter+6)
        if letters == "H":
            conversion = conversion + str(value_of_letter+7)
        if letters == "I":
            conversion = conversion + str(value_of_letter+8)
        if letters == "J":
            conversion = conversion + str(value_of_letter+9)
        if letters == "K":
            conversion = conversion + str(value_of_letter+10)
        if letters == "L":
            conversion = conversion + str(value_of_letter+11)
        if letters == "M":
            conversion = conversion + str(value_of_letter+12)
        if letters == "N":
            conversion = conversion + str(value_of_letter+13)
        if letters == "O":
            conversion = conversion + str(value_of_letter+14)
        if letters == "P":
            conversion = conversion + str(value_of_letter+15)
        if letters == "Q":
            conversion = conversion + str(value_of_letter+16)
        if letters == "R":
            conversion = conversion + str(value_of_letter+17)
        if letters == "S":
            conversion = conversion + str(value_of_letter+18)
        if letters == "T":
            conversion = conversion + str(value_of_letter+19)
        if letters == "U":
            conversion = conversion + str(value_of_letter+20)
        if letters == "V":
            conversion = conversion + str(value_of_letter+21)
        if letters == "W":
            conversion = conversion + str(value_of_letter+22)
        if letters == "X":
            conversion = conversion + str(value_of_letter+23)
        if letters == "Y":
            conversion = conversion + str(value_of_letter+24)
        if letters == "Z":
            conversion = conversion + str(value_of_letter+25)
        if letters == "a":
            conversion = conversion + str(value_of_letter+26)
        if letters == "b":
            conversion = conversion + str(value_of_letter+27)
        if letters == "c":
            conversion = conversion + str(value_of_letter+28)
        if letters == "d":
            conversion = conversion + str(value_of_letter+29)
        if letters == "e":
            conversion = conversion + str(value_of_letter+30)
        if letters == "f":
            conversion = conversion + str(value_of_letter+31)
        if letters == "g":
            conversion = conversion + str(value_of_letter+32)
        if letters == "h":
            conversion = conversion + str(value_of_letter+33)
        if letters == "i":
            conversion = conversion + str(value_of_letter+34)
        if letters == "j":
            conversion = conversion + str(value_of_letter+35)
        if letters == "k":
            conversion = conversion + str(value_of_letter+36)
        if letters == "l":
            conversion = conversion + str(value_of_letter+37)
        if letters == "m":
            conversion = conversion + str(value_of_letter+38)
        if letters == "n":
            conversion = conversion + str(value_of_letter+39)
        if letters == "o":
            conversion = conversion + str(value_of_letter+40)
        if letters == "p":
            conversion = conversion + str(value_of_letter+41)
        if letters == "q":
            conversion = conversion + str(value_of_letter+42)
        if letters == "r":
            conversion = conversion + str(value_of_letter+43)
        if letters == "s":
            conversion = conversion + str(value_of_letter+44)
        if letters == "t":
            conversion = conversion + str(value_of_letter+45)
        if letters == "u":
            conversion = conversion + str(value_of_letter+46)
        if letters == "v":
            conversion = conversion + str(value_of_letter+47)
        if letters == "w":
            conversion = conversion + str(value_of_letter+48)
        if letters == "x":
            conversion = conversion + str(value_of_letter+49)
        if letters == "y":
            conversion = conversion + str(value_of_letter+50)
        if letters == "z":
            conversion = conversion + str(value_of_letter+51)

    return conversion


user_response = input("Would you like to convert a sentence into ASCII values? ")

yes_response = ["YES", "Yes", "yes"]

if user_response in yes_response:
    print(convert(input("Enter a sentence: ")))
else:
    print("Goodbye")






