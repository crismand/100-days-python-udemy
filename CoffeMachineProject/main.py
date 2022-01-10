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
        "cost": 3.0
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 150,
}

profit = 0

def is_resource_sufficient(order_ingredients):
    """Return true of there are enough resources to make the drink the user requested"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """Take payment for the machine"""
    print("Please insert coins.")
    total = 0
    total += int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.10
    total += int(input("How many nickels?")) * 0.05
    total += int(input("How many pennies?")) * 0.01

    return total

def is_transaction_successful(money_received, drink_cost):
    """Return true when payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, that's not enough money.  Money refunded")
        return False

def make_drink(drink_name, ingredients):
    """Deduct required ingredients from resources"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}.")

isOn = True
while isOn:
    choice = input("What would you like? (espresso/latter/cappuccino): ")

    if choice == "off":
        isOn = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk {resources['milk']}ml")
        print(f"Coffee {resources['coffee']}ml")
        print(f"Money ${profit}")
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_drink(choice, drink['ingredients'])
    else:
        print("Sorry, that drink cannot be made by this machine.  Please try again.")