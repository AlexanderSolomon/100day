import random
### Step 1
word_list = ["jamses", "bob", "bonod"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
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

display = []

for i in range(len(chosen_word)):
    display.append("_")
print(display)

    

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

while display != chosen_word:
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
    print(display)


### eller brug position
# for position in range(word_length):
#     letter = chosen_word[position]
#     #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#     if letter == guess:
#         display[position] = letter




#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

#print(display)



#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.


    