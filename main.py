"""
Pursuit Helloworld

This exercise is copied from https://github.com/SmallLion/Python-Projects/blob/main/word_game
"""
import random


LIVES= 5

words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane', 'water']
secret_word = random.choice(words)

clue = list('?????')
HEART_SYMBOL = '\u2764'

GUESSED_WORD_CORRECTLY = False


def update_clue(guessed_letter, secret_word, clue):
    """This method will update the clue if the guess exists in the secret word"""
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1


# A while clause will continue executing until the condition is true.
while LIVES > 0:
    print(clue)
    print('LIVES left: ' + HEART_SYMBOL * LIVES)
    guess = input('Guess a letter or the whole word: ')

    if guess == secret_word:
        GUESSED_WORD_CORRECTLY = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('Incorrect. You lose a life')
        LIVES = LIVES - 1


# Now that we're out of the simple game loop we tell the player whether they've won.
if GUESSED_WORD_CORRECTLY:
    print('You won! The secret word was ' + secret_word)
else:
    print('You lost! The secret word was ' + secret_word)
