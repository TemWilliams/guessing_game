import random
import sys


def start_game():
    print("Welcome to the number guessing game")
    answer = random.randint(1, 10)
    guesses = 1
    guess = None

    while answer != guess:
        try:
            guess = int(input("Please guess a number between 1-10: "))
            if guess > 10 or guess < 1:
                raise ValueError
            elif answer > guess:
                print("Guess higher")
                guesses += 1
            elif answer < guess:
                print("Guess lower")
                guesses += 1
            elif answer == guess:
                print("You got it correct")
                print("You got it in {} tries".format(guesses))
        except ValueError:
            print("oops...please type a number 1-10")

    replay = str(input("Do you want to play again y/n: "))
    if replay.casefold() == "y":
        start_game()
    else:
        sys.exit("Goodbye")


start_game()



