import random
import hangman_art
import list_of_words

# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.


 #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
#------------------#----------DEN HER

 #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

### Step 1
# word_list = ["jamses", "bob", "bonod"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(list_of_words.word_list)
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# print("guess a letter")
# guess = input().lower()
#print(guess)

#TODO-3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
# for letter in chosen_word:
#     if letter == guess:
#         print(True)
#     else:
#         print("Wrong")

"""if guess in chosen_word:
    print(True)
else:
    print(False)"""

### Step 2
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
lives = 6
display = []

for i in range(len(chosen_word)):
    display.append("_")
print(display)

    

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
endOfGame = False


while endOfGame == False and "_"  in display:
    print("guess a letter")
    guess = input().lower()


    index = 0
    while index < len(display):
        for letter in chosen_word:
            if letter == guess:
                display[index]=(guess)
            index += 1
        else:
            index += 1

    if guess not in chosen_word:
        lives -= 1
        print(f"you have {lives} left in the game ")
        if lives == 0:
            endOfGame = True
            print("You lose.")     
    print(display)
    
    if "_" not in display:
        print("YOU WIN")
        endOfGame=True

# else:
#     endOfGame = True
#     print("you won")


### eller brug position
# for position in range(word_length):
#     letter = chosen_word[position]
#     #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#     if letter == guess:
#         display[position] = letter




#TODO-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1. 
#If lives goes down to 0 then the game should stop and it should print "You lose."

 #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(hangman_art.stages[lives])

