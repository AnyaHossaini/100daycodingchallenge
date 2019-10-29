                                                    #Basic Calculator

#Only with whole numbers

num1 = input("enter a number: ")
num2 = input("enter another number: ")

result = int(num1)+int(num2)

print(result)

#Works with floats

num1 = input("enter a number: ")
num2 = input("enter another number: ")

result = float(num1) +float(num2)

print(result)

                                                    #Mad Libs game

#You can enter in a bunch of random words and you take all of those words and put them in a story randomly

print("Roses are red")
print("Violents are blue")
print("I love you")

color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")
print("Roses are "+color)
print(plural_noun + " are blue")
print("I love " + celebrity)

                                                    #Building a Better calculator
num1 = float(input("Enter the first number: "))
op = input("Enter the operator: ")
num2 = float(input("Enter the second number: "))

if op == "+":
   print(num1 + num2)
elif op == "-":
   print(num1 - num2)
elif op == "/":
   print(num1/num2)
elif op == "*":
   print(num1*num2)
else:
   print("invavlid opperator")
                                                   # Building a guessing game
secret_word = "Giraffe"
guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False # You still have guesses left

while guess != secret_word and not(out_of_guesses):
    if guess_count<guess_limit:
        guess = input("Guess the word: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You Lose")
else:
    print("You win")
                                           # Building a translator


def translate(phrase):  # The phrase is what we want to translate

    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":  # If the letter is inside of this then we will translate it
        # we can also say if letter.lower in "aeiou"
                            # if letter.isupper():
                                #translation = translation + "G"

            translation = translation + "g"
        else:
            translation = translation + letter

    return translation


print(translate(input("Enter a phrase: ")))  # letting the user enter the phrase which then will go to the function


