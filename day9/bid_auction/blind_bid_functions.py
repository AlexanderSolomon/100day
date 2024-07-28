import os

bid_dictionary = {}


def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Mac and Linux
    else:
        _ = os.system('clear')  
        
        
        
#enter name and bid
def enter_bid():
    names = input("what is your name \n")    
    bids =input("place your bid (must be an number) \n ")
    bid_dictionary[names]=bids   