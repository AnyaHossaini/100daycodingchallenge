
def play():
    play_game = input("would you like to play game? ")

    if play_game.lower() == "yes":
        print("great")
        guess_word()
    else:
        why_did_you_come()


def guess_word():
    first_word = "majestic"
    print("This word means: having or showing impressive beauty or dignity")
    print("You have 4 chances to guess the word")

    guessing = input("What is your guess? ")

    count = 0
    while guessing.lower() != "majestic" and count < 4:
        print("Incorrect guess, try again")
        guessing = input("What is your guess? ")
        count += 1

    if count == 4:
        play_again = input("You ran out of guessing, play again? ")

        if play_again.lower() == "yes":
            print("Lets try something else")
            easier_game()

        else:
            why_did_you_come()

    if guessing == "majestic":
        print("You got the word!")
        print("You move on to the second game")
        harder_game()


def easier_game():
    print("Okay lets try something else: ")
    print("Find all the 1's in the I")

    print("IIIIIIIIIIIIIIIII1IIIIII1IIIIIIIIII"
          "IIIIIIIIIIIIIIIIIIII1IIIIIIIIIIIIII"
          "IIIII1IIIIIIIIIIIIIIIII1IIIIIIIIIII"
          "IIIIIIIIII1IIIIIIIII1IIIIIII1IIIIII"
          "IIIIIIIIIIIIIII1IIIIIIIII1IIIIIIIII"
          "IIIIIIII1IIIIIIIII1IIIIIIIIII1IIIII"
          "IIIIIIIIIIIII1IIIIIIIII1IIIIIIIIIII")

    find_the_1 = int(input("How many 1's are in the I's?"))

    counter = 0
    while find_the_1 != 15 and counter <4:
        print("Not quite")
        find_the_1 = int(input("How many 1's are in the I's?"))

    if find_the_1 == 15:
        print("You got it!")
        harder_game()
    else:
        print("sorry this is the easiest game I had ")
        why_did_you_come()


def harder_game():
    print("Congrats ! you make it to the next round, lets do riddles now, you have 3 tries this time ")
    guess_what_i_am = input("The more you take, the more you leave behind. What am I?")

    count = 0
    while guess_what_i_am.lower() != "footsteps" and count < 3:
        print("oops, try again!")
        guess_what_i_am = input("The more you take, the more you leave behind. What am I? ")

    if guess_what_i_am.lower() == "footsteps":
        print("You got it!")
        hardest_game()

    else:
        print("Its okay, we can try a different game")
        easier_game()


def hardest_game():
    print("This is the hardest game, if you win this, you win it all!")
    print("Correct the misspelled sentence below in ONE SHOT!")

    correct_the_spelling = input("thsi si a hgu form em ot you ot let you kwon 7 ma thniking fo yuo nad altoughh 7 have"
                                 "nthoing ot asy you kwon 7 hvae thought fo you tdoay")

    if correct_the_spelling == "this is a hug from me to you to let you know 7 am thinking of you," \
                               " and although 7 have nothing to say, you know 7 have thought of you today":
        print("CORRECT")
        winner()


def why_did_you_come():
    print("I don't know why you came")


def winner():
    print("YOU WON")
    print("Today I had an exam and I just want to sleep so, this is the code today.")


if __name__ == "__main__":

    print("Welcome to the game")
    print("Lets begin")
    play()

