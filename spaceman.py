import re
import os
import spacemandrawing

# cleaning up terminal output with lines
line = "\n_______________________________________________________________________________________________\n"

chancesLeft = 7 # number of lives
arrayOfGuessedLetters = [] # init an array of guessed letters
displayWord = [] # init an placeholder word that will hold guessed letters and underscores

def chooseWord():
    os.system('clear')
    print(line) # formatting
    print("\nThis is a two player game.\nFirst, hide the screen from player1.\nWhen that's done, player2 may type in a word you want player1 to guess")
    print(line) # formatting

    waitingForValidWord = True

    while waitingForValidWord == True:
        try:
            global chosenWord
            chosenWord = str(input("Enter a WORD with more than 2 characters for player 2 to guess: ")).upper()
        except:
            print('Unexpected error. Try something else')

        # if chosenWord == '\x00':
        if (len(chosenWord) > 0) and chosenWord.isalpha():  # check if input is only a single character and a letter
            waitingForValidWord = False
        else:
            waitingForValidWord = True

    print(line) # formatting
    os.system('clear')

chooseWord()

def showGameInstructions():
    # show instructions
    print("\nWelcome to Spaceman! A word has been chosen that YOU must guess, one letter at a time.")
    print("If you guess incorrectly 7 times, you lose and your friend gets launched into space!")
    print("If you guess all letters correctly, you save your friend from eternal loneliness.\n")
    print("Alright, let's get started! Here is your word:\n")

showGameInstructions()

def hideWord():
    for char in chosenWord:
        displayWord.append("_ ") # replace letters in chosenWord with underscores and store that inside displayWord

hideWord()
print(''.join(displayWord)) # show randomly chosen word, except with letters are replaced with underscores

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

    waitingForValidLetter = True

    while waitingForValidLetter:
        try:
            letterInput = input(str("\nGuess a single letter: "))
        except:
            print('Unexpected error. Try something else')

        if (len(letterInput) == 1) and letterInput.isalpha():  # check if input is only a single character and a letter
            checkAndPrint(letterInput)
            waitingForValidLetter = False

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
