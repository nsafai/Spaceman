
# number of lives
guessesRemaining = 7

# init an array with a list of words
arrayOfWords = ["Apple", "Orange", "Banana", "Grapes", "Mango", "Raspberry"]

# choose a word randomly (chosenWord)
chosenWord = arrayOfWords[0]

# init an array of guessed letters
arrayOfGuessedLetters = "pE"

# init an placeholder word that will hold guessed letters and underscores
placeholderWord = []

# show instructions
print("\nWelcome to Spaceman! We've taken the liberty of choosing a word for you. Your job is to guess that word, one letter at a time.")
print("If you guess incorrectly 7 times, you lose and your friend gets launched into space! If you guess all letters correctly, you save your friend from eternal loneliness.\n")
print("Alright, let's get started! Here is your word:\n")

# playing = True
# while playing:
#     print('playing!')

def checkAndPrint():
    global guessesRemaining
    for char in chosenWord:
        if char.upper() in arrayOfGuessedLetters.upper():
            placeholderWord.append(char.upper() + " ")
        else:
            placeholderWord.append("_ ")
            guessesRemaining = guessesRemaining - 1

    print(''.join(placeholderWord))

checkAndPrint()
# show randomly chosen word, except with letters are replaced with underscores
# ask user for a letter input (v2: only allow one letter at a time)
#     add letter inputs to an arrayOfGuessedLetters
#     if chosenWord contains input, replace underscores with Letter input
#     else
#         remove 1 from guessesRemaining
#         show all letter inputs so far (if incorrect, follow by ("✗"), else do not)
#         draw the next spaceman thing
#
# if guessesRemaining = 0: Game Over
