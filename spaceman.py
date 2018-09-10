import re
import os
import spacemandrawing

# cleaning up terminal output with lines
line = "\n_______________________________________________________________________________________________\n"

# number of lives
chancesLeft = 7

os.system('clear')
print(line) # formatting
chosenWord = input("\n\nThis is a two player game.\nFirst, hide the screen from player1.\nWhen that's done, player2 may type in a word you want player1 to guess: ").upper()
print(line) # formatting
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
    os.system('clear') # clear terminal
    global chancesLeft
    print(line) # formatting

    # check where guessedLetter appears in chosenWord (outputs indices, or, if guess is incorrect, is empty)
    indicesForCorrectGuesses = [m.start() for m in re.finditer(guessedLetter, chosenWord)]

    if indicesForCorrectGuesses == []: # guessed incorrectly
        print("Noooope, sucks to suck. You lost a life! What else would you like to guess?")
        chancesLeft -= 1 # check if already entered that letter
    else:
        # correct guess
        print('Niiiiiice! That letter is indeed in the word :)')

        for i in indicesForCorrectGuesses: # for every correct guess
            displayWord[i] = guessedLetter # replace underscores with correctly guessed letters

    print(line) # formatting

    print("You have %d chance(s) left\n" % chancesLeft) # show remaining tries

    arrayOfGuessedLetters.append(guessedLetter) # add most recent guess to array of all guessed letters
    print("Guesses so far: " + ' '.join(arrayOfGuessedLetters) + "\n") # print all guesses

    print(' '.join(displayWord)) # show progress so far

    print(line) # formatting

    spacemandrawing.drawSpaceMan(chancesLeft)

def askForUserInput():

    waitingForInput = True

    while waitingForInput == True:
        textInput = input(str("\nGuess a single letter: "))

        if (len(textInput) == 1):  # check if input is only a single character
            checkAndPrint(textInput)
            waitingForInput = False
        else:
            waitingForInput = True

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
