#!/usr/bin/env python3
from random import randint


"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""

def main():
    num= randint(1,100)
    guess= 0
    rounds= 0

    while rounds < 5 and guess != num:
        guess= input("Guess a number between 1 and 100\n>")

        # COOL CODE ALERT: what is the purpose of the next four lines?
        if guess.isdigit():
            guess= int(guess)
        else:
            continue

        if guess > num:
            print("Too high!")
            rounds += 1
            continue

        if guess < num:
            print("Too low!")
            rounds += 1
            continue

        else:
            print("Correct!")
            break
if __name__  == "__main__":
    main()
