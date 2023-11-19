#rules:
#rock wins over scissors
#scissors wins ocer paper
#paper wins over rock


#import random
#import random
#logic where who beats who

rock = "0rock"

scissor ="1scissor"

paper = "2paper"




print( "choose your weapon travelor :) ")

pc_choice = 0
print(pc_choice)
choose_weapon = int(input("select 0 for Rock, 1 for scissor, 2 for paper: \n"))
print("you chose: ", choose_weapon)
if pc_choice == 0 and choose_weapon == 1:  
    print(f"you choose + {scissor} + pc has choosen + {rock} +  therefore you loose game over")
elif pc_choice == 0 and choose_weapon == 0:
    print("its a draw try again")
elif pc_choice == 0 and choose_weapon == 2:
    print(f"YOU WIN " + rock + "looses to " + paper)
else:
    print("invalid")


# print("Choose your weapon, traveler :) ")

# pc_choice = 0  # Computer's choice is always 0 (Rock)
# print("PC chose:", pc_choice)

# choose_weapon = int(input("Select 0 for Rock, 1 for Scissors, 2 for Paper: \n"))
# print("You chose:", choose_weapon)

# rock = "Rock"
# scissors = "Scissors"
# paper = "Paper"

# if pc_choice == 0 and choose_weapon == 1:
#     print(f"You chose {scissors}, PC chose {rock}. You lose! Game over.")
# elif pc_choice == 0 and choose_weapon == 0:
#     print("It's a draw. Try again.")
# elif pc_choice == 0 and choose_weapon == 2:
#     print(f"You win! {rock} loses to {paper}.")
# else:
#     print("Invalid input or not implemented case.")


       
    

        


