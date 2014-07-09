# Number guessing game

import random

secret = random.randint(1,10)
guess = 0
attempts = 0

while secret != guess:

    guess = int(input("Guess a number between 1 and 10: "))
    attempts = attempts + 1;

    if (guess == secret):
        print("You found the secret number", secret, "in", attempts, "attempts")
        quit()
    elif (guess > secret):
        print("Your guess is high, try again")

    else:
        print("Your guess is low, try again")
