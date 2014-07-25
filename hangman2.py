# Classic Hangman Game!

import random

#first create your list of hangman
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   |
 |   |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |
----------
""")

#print(HANGMAN[0])

#max number of wrong guesses a player can do?
# player only 1 minus total number of chances
MAXWRONG = len(HANGMAN) - 1

# tuple containing words, add more words to your liking
# keep letters to lower letters for easy comparison
WORDS = ("hello", "light", "bulb")

word = random.choice(WORDS) # random word to be guessed
guesses = "_" * len(word) # one dash for each letter in the word to be guessed
wrong = 0
used = []

while wrong < MAXWRONG and guesses != word:
    print(HANGMAN[wrong])
    print("You have used the following letters", used)
    print("The guess is: ", guesses)

    guess = input("Please type your guess: ").lower() #make input lower

    while guess in used:
        print("You have already guessed the letter: ", guess)
        guess = input("Please type your guess: ").lower() #make input lower

    used.append(guess)

    if (guess in word):
        print("This letter is in the word: ")

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += guesses[i]
        guesses = new
    else:
        wrong += 1
        print("Sorry,", guess, "is not in the word, wrongs used are: ", wrong)

if wrong == MAXWRONG:
    print(HANGMAN[wrong])
    print("You have been hanged, Better Luck Next Time, the word was", word)

else:
    print("You guessed it right!, Congrats!!", word)


