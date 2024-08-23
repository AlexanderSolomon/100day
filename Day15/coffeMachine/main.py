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


# Money in the machine
#money = 0


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
    print(f"Coffe: {resources['coffee']}.g  \nMilk: {resources['milk']}.ml \nWater: {resources['water']}.ml \nMoney: {resources['money']}$")


# TODO Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
"""
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.
"""
# while machine == True:
#     coffeChoise = input("would you like: 1. Espresso, 2.Latte or 3.Cappucino \n")
#     if coffeChoise == "1":
#         print("you choose espresso")
#     elif coffeChoise == "2":
#         print("you choose latte")
#     elif coffeChoise == "3":
#         print("you choose cappucino")
#     elif coffeChoise == "off":
#         machine = False
#     elif coffeChoise == "report":
#         report()

# TODO Turn off the Coffee Machine by entering “off” to the prompt.  DONE
"""
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. 
Your code should end execution when this happens
"""

# TODO Check resources sufficient?
"""
a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”
c. The same should happen if another resource is depleted, e.g. milk or coffee."""

#print(resources["coffee"] -20)

#espresso 
def espresso():
    resources["water"] -= 50 
    resources["coffee"] -= 18
    resources["money"] += 1.5

def latte():
    resources["water"] -= 200
    resources["milk"] -= 150
    resources["coffee"] -= 18
    resources["money"] += 2.5


print(resources)
espresso()
print(resources)
latte()
print(resources)

#latte


#cappuccino
