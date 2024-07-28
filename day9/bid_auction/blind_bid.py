import art as art
import blind_bid_functions as blind_bid_functions


print(art.logo)
more_members =0

while more_members == 0:
    blind_bid_functions.enter_bid()
    print(blind_bid_functions.bid_dictionary)

    answer = input("are there more bids? press y if not press n \n ")
    if answer == "y": 
        blind_bid_functions.clear_screen()
        print("next person")

    else:
        print("the winner is: ")
        winner = print(max(blind_bid_functions.bid_dictionary))
        more_members += 1
        

    


 


