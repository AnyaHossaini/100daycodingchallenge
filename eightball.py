""""
8 ball magic game
"""

import random

answer_options = ["Your going to meet a panda in your dreams.", "Bananas are always bums",
                  "Its either blue or it might be 62", "The answer to life is 42",
                  "Tbh Anya is a loner, that's most important to fix", "Everything is a lie",
                  "Potatoes are botanically classified as a vegetable, "
                  "but they are classified nutritionally as a starchy food,", "Oreo flavored oreos are"
                  "something we need in life"]


def game():
    while user_decides != "I'm gonna go...":

        first_question = input("If you farted alone did you really fart? yupp for yes or nahh for no- ")
        if first_question == "yupp":
            print(random.choice(answer_options))

        else:
            print("You couldn't be more wrong in life... your farts probably smell the worst")

        second_question = input("Is a hot dog a sandwich ? Sorta... for yes or tf you talkin about for no- ")
        if second_question == "Sorta...":
            print(random.choice(answer_options))
        else:
            print("Well then what is it ? Hotdog has bread.. and something in between in! You're nonsense -")

        third_question = input("Could many chickens kill a elephant? We could test it for a possible yes or nope for no-  ")
        if third_question == "We could test it for a possible":
            print(random.choice(answer_options))
        else:
            print("Well you have no FAITH huh")

        fourth_question = input("If a pancake is made inside a cup would it still be a pancake?yes or no-  ")
        if fourth_question == "yes":
            print(random.choice(answer_options))
        else:
            print("Are you a chef?")

        fifth_question = input("If the earth is completely round, have we made anything straight ? yes or no- ")
        if fifth_question == "yes":
            print(random.choice(answer_options))
        else:
            print("Well clearly...")

        sixth_question = input("If a sheep sneezes do the other sheep sneeze with it? yes or  no- ")
        if sixth_question == "yes":
            print(random.choice(answer_options))
        else:
            print("How would you know?")

        seventh_question = input("If you replace  everyone on a team over time is it still the same team? yes or no -")
        if seventh_question == "yes":
            print(random.choice(answer_options))
        else:
            print("Well you must feel special ")

        eighth_question = input("Is air water that isn't wet? yes or no")
        if eighth_question == "yes":
            print(random.choice(answer_options))
        else:
            print("Well lets think about that answer")


def its_done():
    print("Well that's all")


if __name__ == "__main__":
    print("time to play")
    user_decides = input("Ready to play? if yes type: You’re not giving me that much of a choice, huh? \n" \
                         "if no type: I'm gonna go...  ")
    if user_decides == "You’re not giving me that much of a choice, huh?":
        game()
        its_done()
    else:
        "Well damn, bye tho"



