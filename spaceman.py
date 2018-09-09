import re

# number of lives
chancesLeft = 7

# init an array with a list of words
arrayOfWords = ["Apple", "Orange", "Banana", "Grapes", "Mango", "Raspberry"]

# choose a word randomly (chosenWord)
chosenWord = arrayOfWords[0]

# init an array of guessed letters
arrayOfGuessedLetters = []

# init an placeholder word that will hold guessed letters and underscores
displayWord = []

# show instructions
print("\nWelcome to Spaceman! We've taken the liberty of choosing a word for you. Your job is to guess that word, one letter at a time.")
print("If you guess incorrectly 7 times, you lose and your friend gets launched into space! If you guess all letters correctly, you save your friend from eternal loneliness.\n")
print("Alright, let's get started! Here is your word:\n")

# show randomly chosen word, except with letters are replaced with underscores
def hideWord():
    for char in chosenWord:
        displayWord.append("_ ")

hideWord()
print(''.join(displayWord))

def checkAndPrint(guessedLetter):
    global chancesLeft
    print(guessedLetter)

    

    indicesForCorrectGuesses = [m.start() for m in re.finditer(guessedLetter, chosenWord)]

    elif indicesForCorrectGuesses == []:
        print("nope sucks to suck")

    else:
        # correct guess
        print('naiiice')
        for i in indicesForCorrectGuesses:
            displayWord[i] = guessedLetter

    print(' '.join(displayWord))

    # for char in chosenWord:
    #     if char.upper() == guessedLetter:
    #         displayWord.append(char.upper() + " ")
    #     else:
    #         chancesLeft = chancesLeft - 1
    #
    # arrayOfGuessedLetters.append(guessedLetter)
    # print("Guesses so far: " + ''.join(arrayOfGuessedLetters))
    # print(''.join(displayWord))

def askForUserInput():
    checkAndPrint(input("Guess a letter: "))

playing = True
while playing:
    askForUserInput()
    # if guessed full word, gameOver
    # else: ask for user input

# checkAndPrint()

# ask user for a letter input (v2: only allow one letter at a time)
#     add letter inputs to an arrayOfGuessedLetters
#     if chosenWord contains input, replace underscores with Letter input
#     else
#         remove 1 from chancesLeft
#         show all letter inputs so far (if incorrect, follow by ("✗"), else do not)
#         draw the next spaceman thing
#
# if chancesLeft = 0: Game Over
