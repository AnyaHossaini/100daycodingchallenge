"""
Madlib game

NOT COMPLETE
"""

#CONSTANTS
INTRO_PHRASE = "Please give me a "


def story_to_start():

    starting_story = int(input("We have 5 stories! Which story would you like to begin with? "))

    while starting_story <= 0 or starting_story >= 6:
        print("Oops, looks like you want more stories! We only have 1 - 5 try again")
        starting_story = int(input("We have 5 stories! Which story would you like to begin with? "))

    if starting_story == 1:
        first_story()

    if starting_story == 2:
        second_story()

    if starting_story == 3:
        third_story()

    if starting_story == 4:
        fourth_story()

    if starting_story == 5:
        fifth_story()


def first_story():
    print("Welcome to the world's worst bedtime story!")

    a_place = input(INTRO_PHRASE + "place: ")
    adj = input(INTRO_PHRASE + "adjective: ")
    celeb = input(INTRO_PHRASE + "celebrity: ")
    body_part = input(INTRO_PHRASE + "body part: ")
    organ = input(INTRO_PHRASE + "human organ: ")
    adj2 = input(INTRO_PHRASE + "adjective: ")
    celeb2 = input(INTRO_PHRASE + "celebrity: ")
    adj3 = input(INTRO_PHRASE + "adjective: ")
    body_part2 = input(INTRO_PHRASE + "body part: ")
    body_part3 = input(INTRO_PHRASE + "body part: ")
    a_place2 = input(INTRO_PHRASE + "place: ")


def second_story():
    print(" Welcome to the zoo !")

    adj = input(INTRO_PHRASE + "adjective: ")
    noun = input(INTRO_PHRASE + "noun: ")
    verb_past = input(INTRO_PHRASE + "verb (past tense): ")
    adverb = input(INTRO_PHRASE + "adverb")
    adj2 = input(INTRO_PHRASE + "adjective")
    noun2 = input(INTRO_PHRASE + "noun: ")
    noun3 = input(INTRO_PHRASE + "noun: ")
    adj3 = input(INTRO_PHRASE + "adjective: ")
    verb = input(INTRO_PHRASE + "verb: ")
    adverb2 = input(INTRO_PHRASE + "adverb: ")
    verb_past2 = input(INTRO_PHRASE + "verb(past tense): ")
    adj4 = input(INTRO_PHRASE + "adjective: ")

    print("Today I went to the zoo. I saw a(n) ", adj, noun, "\n"
          "jumping up and down in its tree. He ", verb_past, adverb + "\n"
          "through the large tunnel that led to its ", adj2, noun2 + "\n"
          "I got some peanuts and passed them through the cage to a gigantic gray\n"
          , noun3 + "towering above my head. Feeding that animal made me hungry.\n"
          "I went to get a", adj3 + "scoop of ice cream. It filled my stomach.\n"
          " Afterwards I had to ", verb, adverb2 + "to catch our bus. \n"
          "When I got home I ", verb_past2," my mom for a ", adj4, " day at the zoo.")

    do_another()


def third_story():
    print(" Welcome to the fun park !")
    adj = input(INTRO_PHRASE + "adjective: ")
    plural_noun = input(INTRO_PHRASE + "plural noun: ")
    noun = input(INTRO_PHRASE + "noun: ")
    adverb = input(INTRO_PHRASE + "adverb: ")
    number = input(INTRO_PHRASE + "number: ")
    past_tense_verb = input(INTRO_PHRASE + "past tense verb: ")
    est_adjective = input(INTRO_PHRASE + "-est adjective: ")
    past_tense_verb2 = input(INTRO_PHRASE + "past tense verb: ")
    adj2 = input(INTRO_PHRASE + "adjective: ")

    print("Today, my fabulous camp group went to a (an) ", adj, " amusement park.\n"
          "It was a fun park with lots of cool ", plural_noun, " and enjoyable play structures.\n"
          "When we got there, my kind counselor shouted loudly, Everybody off the ", noun,  "\n"
          "We all pushed out in a terrible hurry. My counselor handed out yellow tickets,\n"
          "and we scurried in. I was so excited! I couldn't figure out what exciting \n"
          "thing to do first. I saw a scary roller oaster I really liked so, I ", adverb, "\n"
          "ran over to get in the long line that had about", number, "people in it.\n"
          " When I finally got on the roller coaster I was", past_tense_verb, "\n"
          "In fact I was so nervous my two knees were knocking together. This was the\n"
          , est_adjective, "ride I had ever been on! In about two minutes I heard the\n"
          "crank and grinding of the gears. That’s when the ride began! When I got to the bottom,\n"
          "I was a little", past_tense_verb2, "but I was proud of myself. The rest of the day went\n"
          , adverb, " It was a(n)", adj2)

    do_another()
    

def fourth_story():
    print()


def fifth_story():
    print()


def do_another():

    do_another_story = input("would you like to do another ?")

    if do_another_story.lower() == "yes" or do_another_story.lower() == "y":
        print("Great, let's do another one")
        story_to_start()

    else:
        exit_out()


def exit_out():
    print("Thanks for playing! Bye")


if __name__ == "__main__":

    print("Welcome to madlib story game!")
    play_game = input("Would you like to play? ")

    if play_game.lower() == "yes" or play_game.lower() == "y":
        print("Great, let's get started")
        story_to_start()

    else:
        exit_out()

