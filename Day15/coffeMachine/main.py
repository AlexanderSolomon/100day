
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# machine true = on
machine = True   




# print(f"{MENU['cappuccino'].get('cost')}")
# print(f"{MENU['espresso'].get('cost')}")
# print(f"{MENU['latte'].get('cost')}")

# TODO Print report.
"""
a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
"""
def report():
    print(f"Coffee: {resources['coffee']}.g  \nMilk: {resources['milk']}.ml \nWater: {resources['water']}.ml \nMoney: {resources['money']}$")

# TODO Check resources sufficient?
"""
a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”
c. The same should happen if another resource is depleted, e.g. milk or coffee."""
#espresso 
def espresso():
    if resources["water"]< 50:
        print("insufficient resources")
    elif resources["coffee"]<18:
        print("insufficient resources")  
    else:
        resources["water"] -= 50 
        resources["coffee"] -= 18
        resources["money"] += 1.5
        print("enjoy your espresso")

def latte():
    if resources["water"]< 200:
        print("insufficient resources")
    elif resources["coffee"]<24:
        print("insufficient resources")  
    elif resources["milk"]<150:
        print("insufficient resources")  
    else:
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
        resources["money"] += 2.5
        print("enjoy your latte")

def cappucino():
    if resources["water"]< 250:
        print("insufficient resources")
    elif resources["coffee"]<24:
        print("insufficient resources")  
    elif resources["milk"]<100:
        print("insufficient resources")  
    else:
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24
        resources["money"] += 3.0
        print("enjoy your cappucino")


# TODO Process coins
""".
a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52"""
def takePayment():
    print("insert coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    print(total)
    return total


"""6. Check transaction successful?
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “Sorry that's not enough money. Money refunded.”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.
E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places."""


def check_payment():
    total = takePayment()
    if coffeChoise == "3" :
        cost = MENU['cappuccino'].get('cost')
    elif coffeChoise == "2" :
        cost = MENU['latte'].get('cost')
    elif coffeChoise == "1" :
        cost = MENU['espresso'].get('cost')

    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = total - cost
        print(f"Payment accepted. Your change is ${change:.2f}.")
        

            

# TODO Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
"""
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.
"""

while machine == True:
    coffeChoise = input("would you like: 1. Espresso, 2.Latte or 3.Cappucino \n")
    if coffeChoise == "1":
        print("you choose espresso")
        check_payment()
        espresso()
    elif coffeChoise == "2":
        print("you choose latte")
        check_payment()
        latte()
    elif coffeChoise == "3":
        print("you choose cappucino")
        check_payment()
        cappucino()
    elif coffeChoise == "off":
        machine = False
    elif coffeChoise == "report":
        report()

# TODO Turn off the Coffee Machine by entering “off” to the prompt.  DONE
"""
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. 
Your code should end execution when this happens
"""


#testing the subtractions
# print(resources)
# espresso()
# print(resources)
# latte()
# print(resources)

#latte


#cappuccino
