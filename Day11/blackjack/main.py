import random
import clear_stuff
import art 
#creating a black jack game
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

print(art.logo)
player = []
house = []
cards =[1,2,3,4,5,6,7,8,9,10,10,10,10,11]


    
#get a random number (card) from the list 
def deal_1_card():
    card1 = random.choice(cards)
    return card1

#deal 2 cards to player and house 
def deal_hands():
    p1_hand= deal_1_card()
    player.append(p1_hand)
    p2_hand= deal_1_card()
    player.append(p2_hand)
    print(f"players cards {player}")
    print(sum(player))
    
    
    
    c1_hand= deal_1_card()
    house.append(c1_hand)
    c2_hand= deal_1_card()
    house.append(c2_hand)
    print(f"house was dealt {house[0]} - ")
    #print(f"house sum is {sum(house)}")

#player gets card
def hit_me():
    extra_card = random.choice(cards)
    print(extra_card)
    if extra_card == 11 and sum(player) > 12:
        player.append(1)
    else:
        player.append(extra_card)
    return print(f"you recieved a {extra_card} \n if the sum was above 12 and the cards was 11 u get a 1 \n and the total is: {sum(player)}")
#house gets card
def hit_me_house():
    extra_card = random.choice(cards)
    house.append(extra_card)
    return print(f"house recieved a {extra_card} and the total is: {sum(house)}")

#house logic when to draw
def House_Game_mode():
    print(f"house starts with: {house} total of {sum(house)}")
    while sum(house) < 17:
        print("house has less than 17 so HIT ")
        hit_me_house()
    if sum(house) > 16 and sum(house) < 21:
        print("house stands")
    if sum(house) >21:
        print(f"house bust with {sum(house)}")
        
     

def distance_from_21():
    total_player = sum(player)
    player_distance_from_21 = (21 - total_player)
    #print(f" your distance {player_distance_from_21}")

    total_house = sum(house)
    house_distance_from_21 = (21 - total_house)
    #print(f" house distance {house_distance_from_21}")
    
    if player_distance_from_21 == house_distance_from_21:
        print(f"DRAW player got {sum(player)} and dealer got {sum(house)}")
        
    elif player_distance_from_21 > house_distance_from_21 and sum(house)< 22:
        print(f"dealer wins with {sum(house)} over {sum(player)}")
        
    else:
        print(f" player wins with {sum(player)} over {sum(house)}")
        return

    
def game_on():
    player_select =input("want to play? then press 1 \npress 0 to close the game \n")
    if player_select == "1":
        game_state == True
    else:
        game_state== False


# print(player, sum(player))
# deal_hands()
# print(player, sum(player))

# hit_me()
# print(player, sum(player))

# hit_me()
# print(player, sum(player))

options = {"1 start new game": deal_hands, "2 hit me": hit_me, "3 Stand": distance_from_21}
options2 = { "2 hit me": hit_me, "3 Stand": distance_from_21}

game_state = True



while game_state == True:
    player_select =input("press 1 to start new game \npress 0 to close the game \n")
    clear_stuff.clear_screen()
    if player_select == "0":
        break
    
    if player_select == "1":
        print("here is your starting hand")
        player = []
        house = []
        deal_hands()
    if sum(house) == 21:
        print("you loose HOUSE got 21")
        continue 
    elif sum(player) == 21 and sum(house) < 21:
        print("player wins BLACK JACK  ")
        continue
    
    for key in options2:
        print(key)
    player_select =input("press 2 to get a card \npress 3 to stand \n")
    
    while player_select =="2":
        hit_me()
        print(player, sum(player))
        if sum(player)> 21:
            print("BUST over 21 you loose") 
            break
        elif sum(player) == 21 and sum(house) < 21:
            print("player wins BLACK JACK ")
            break
        for key in options2:
            print(key)
        player_select =input("press 2 to get a card \npress 3 to stand \n")

    if player_select == "3":
        House_Game_mode()
        distance_from_21()
        
        
    


# TODO 


## Complete 
# If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
# After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start.
# Compare user and computer scores and see if it's a win, loss, or draw.
# Once the user is done and no longer wants to draw any more cards, let the computer play. The computer should keep drawing cards unless their score goes over 16.
# Detect when computer or user has a blackjack. (Ace + 10 value card).
# If computer gets blackjack, then the user loses (even if the user also has a blackjack). If the user gets a blackjack, then they win (unless the computer also has a blackjack).
# Reveal computer's first card to the user.
# Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.
# Deal both user and computer a starting hand of 2 random card values.
# Ask the user if they want to get another card.
# Calculate the user's and computer's scores based on their card values.
# Print out the player's and computer's final hand and their scores at the end of the game.
