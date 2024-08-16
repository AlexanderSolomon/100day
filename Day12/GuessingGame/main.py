import random
import art

print(art.logo)

print("Welcome to the Guessing Game!")
print("I am thinking of a number between 1 and 100.")

# get a random number between 1 and 100 that is hidden
### random_number = random.randint(1,100)

# guess = input("Make a guess")
# print("Too high")
# print("Too low")
# print("Guess again")
# print("You have (x) attempts remaining")

######----------------------------#######



# # easy level 10 attempts to guess number

# def easy_mode():
#     random_number = random.randint(1,100)
#     attempts = 10
#     while attempts > 0:
#         print(f"you have {attempts} attempts to guess the number")
#         guess = int(input("Make a guess: "))
#         if guess == random_number:
#             print("you Win")
#             break
#         elif guess > random_number:
#             print("Too high  try again")
#             attempts -= 1
#             if attempts < 1:
#                 print("you loose")
#                 break
#         elif guess < random_number:
#             print("Too low  try again")
#             attempts -= 1
#             if attempts < 1:
#                 print("you loose")
#                 break

# # hard has 5 attempts to guess number
# def hard_mode():
#     random_number = random.randint(1,100)
#     attempts = 5
#     while attempts > 0:
#         print(f"you have {attempts} attempts to guess the number")
#         guess = int(input("Make a guess: "))
#         if guess == random_number:
#             print("you Win")
#             break
#         elif guess > random_number:
#             print("Too high  try again")
#             attempts -= 1
#             if attempts < 1:
#                 print("you loose")
#                 break
#         elif guess < random_number:
            # print("Too low  try again")
            # attempts -= 1
            # if attempts < 1:
            #     print("you loose")
            #     break

# game_mode()

######----------------------------#######

# easy or hard
def game_mode():
    difficulty = input("Type easy or hard \n: ").lower()
    if difficulty == "easy":
        return play_game(10)
        
    elif difficulty == "hard":
        return play_game(5)
        
    else:
        print("invalid input")


def play_game(attempts):
    random_number = random.randint(1, 100)
    while attempts > 0:
        print(f"You have {attempts} attempts to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print("You win!")
            return
        elif guess > random_number:
            print("Too high. Try again.")
        else:
            print("Too low. Try again.")
        attempts -= 1
    
    print(f"You lose. The correct number was {random_number}.")




game_mode()