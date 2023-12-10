#rules:
#rock wins over scissors
#scissors wins ocer paper
#paper wins over rock


#import random
#import random
#logic where who beats who
import random

rock = "0rock"

scissor ="1scissor"

paper = "2paper"




print( "choose your weapon travelor :) ")

pc_choice = random.randint(0,2)
print(pc_choice)
choose_weapon = int(input("select 0 for Rock, 1 for scissor, 2 for paper: \n"))
print("you chose: ", choose_weapon)
if pc_choice == 0 and choose_weapon == 1:  
    print(f"you choose + {scissor} + pc has choosen + {rock} +  therefore you loose game over")
elif pc_choice == 0 and choose_weapon == 0:
    print("its a draw try again")
elif pc_choice == 0 and choose_weapon == 2:
    print(f"YOU WIN " + rock + "looses to " + paper)
if pc_choice == 1 and choose_weapon == 2:  
    print(f"you choose + {paper} + pc has choosen + {scissor} +  therefore you loose game over")
elif pc_choice == 1 and choose_weapon == 1:
    print("its a draw try again")
elif pc_choice == 1 and choose_weapon == 0:
    print(f"YOU WIN " + scissor + "looses to " + rock)
if pc_choice == 2 and choose_weapon == 0:  
    print(f"you choose + {rock} + pc has choosen + {paper} +  therefore you loose game over")
elif pc_choice == 2 and choose_weapon == 2:
    print("its a draw try again")
elif pc_choice == 2 and choose_weapon == 1:
    print(f"YOU WIN " + paper + "looses to " + scissor)




        


