import re
import os

# cleaning up terminal output with lines
line = "\n_______________________________________________________________________________________________\n"

# number of lives
chancesLeft = 7

# init an array with a list of words
# arrayOfWords = ["Apple", "Orange", "Banana", "Grapes", "Mango", "Raspberry", "Zebra", "Cheesy"]

os.system('clear')
chosenWord = input("This is a two player game.\nFirst, hide the screen from player1.\nWhen that's done, player2 may type in a word you want player1 to guess: ").upper()
os.system('clear')

# init an array of guessed letters
arrayOfGuessedLetters = []

# init an placeholder word that will hold guessed letters and underscores
displayWord = []

# show instructions
print("\nWelcome to Spaceman! A word has been chosen that YOU must guess, one letter at a time.")
print("If you guess incorrectly 7 times, you lose and your friend gets launched into space!")
print("If you guess all letters correctly, you save your friend from eternal loneliness.\n")
print("Alright, let's get started! Here is your word:\n")

# show randomly chosen word, except with letters are replaced with underscores
def hideWord():
    for char in chosenWord:
        displayWord.append("_ ")

hideWord()
print(''.join(displayWord))

def checkAndPrint(guessedLetter):
    guessedLetter = guessedLetter.upper()
    os.system('clear')
    global chancesLeft
    print(line)

    # check where guessedLetter appears in chosenWord (outputs indices)
    indicesForCorrectGuesses = [m.start() for m in re.finditer(guessedLetter, chosenWord)]

    if indicesForCorrectGuesses == []:
        print("Noooope, sucks to suck. You lost a life! What else would you like to guess?")
        # check if already entered that letter
        chancesLeft -= 1
    else:
        # correct guess
        print('Niiiiiice! That letter is indeed in the word :)')

        # add letter inputs to an arrayOfGuessedLetters
        for i in indicesForCorrectGuesses:
            displayWord[i] = guessedLetter

    print(line)

    # show remaining tries
    print("You have %d chance(s) left\n" % chancesLeft)


    # show all letter inputs so far (if incorrect, follow by ("✗"), else do not)
    arrayOfGuessedLetters.append(guessedLetter)
    print("Guesses so far: " + ''.join(arrayOfGuessedLetters) + "\n")


    # show progress so far
    print(' '.join(displayWord))

    # draw spaceman

def askForUserInput():
    # ask user for a letter input (v2: only allow one letter at a time)
    checkAndPrint(input(str("\nGuess a letter: ")))

playing = True
while playing:
    if chancesLeft == 0:
        print("Oh no, you ran out of guesses. The word was %s \n" % chosenWord)
        print("Try again sometime :)\n")
        playing = False

    elif chosenWord == ''.join(displayWord):
        # if guessed full word, gameOver
        print("You win! Please play again sometime :)\n")
        playing = False
    # else:
    else:
        # if not guessed correctly keep asking for user input until
        askForUserInput()




#
# if chancesLeft = 0: Game Over
