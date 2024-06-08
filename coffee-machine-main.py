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
}

# TODO: 3. Print Report

resources["money"] = 0


def print_report():
    for item in resources:
        if item == "water" or item == "milk":
            print(f"{item.capitalize()}: {resources[item]}ml")
        elif item == "coffee":
            print(f"{item.capitalize()}: {resources[item]}g")
        elif item == "money":
            print(f"{item.capitalize()}: ${resources[item]}")


# TODO: 4. Check resources sufficient?
def resource_check(water, milk, coffee):
    if resources["water"] < water:
        print("Sorry there is not enough water.")
        return False
    elif resources["milk"] < milk:
        print("Sorry there is not enough milk.")
        return False
    elif resources["coffee"] < coffee:
        print("Sorry there is not enough coffee.")
        return False
    return True


# TODO: 5. Process Coins
def amount_entered(pennies, nickles, dimes, quarters):
    pennies = pennies * 0.01
    nickles = nickles * 0.05
    dimes = dimes * 0.1
    quarters = quarters * 0.25
    return pennies + nickles + dimes + quarters


coffee_machine_on = True
while coffee_machine_on:
    # TODO: 1. Ask user what would they like to have (espresso/latte/cappuccino)
    user_choice = input("What would you like? (espresso/latte/cappuccino) ")

    # TODO: 2. Turn off the machine by entering off
    if user_choice.lower() == "off":
        coffee_machine_on = False

        # Add money
    elif user_choice.lower() == "report":
        print_report()

    elif user_choice in MENU:
        if resource_check(water=MENU[user_choice]["ingredients"].get("water", 0),
                          milk=MENU[user_choice]["ingredients"].get("milk", 0),
                          coffee=MENU[user_choice]["ingredients"]["coffee"]):
            print("Please insert coins.")
            quarters = float(input("How many quarters: "))
            dimes = float(input("How many dimes: "))
            nickles = float(input("How many nickles: "))
            pennies = float(input("How many pennies: "))

            # TODO: 6. Check transaction Successful
            total_money = amount_entered(pennies, nickles, dimes, quarters)
            if total_money >= MENU[user_choice]["cost"]:
                change_amount = round(total_money - MENU[user_choice]["cost"], 2)
                resources["water"] = resources["water"] - MENU[user_choice]["ingredients"].get("water",0)
                resources["milk"] = resources["milk"] - MENU[user_choice]["ingredients"].get("milk", 0)
                resources["coffee"] = resources["coffee"] - MENU[user_choice]["ingredients"].get("coffee",0)
                resources["money"] += MENU[user_choice]["cost"]
                print(f"Here is ${change_amount} in change.")
                print(f"Here is your {user_choice}. Enjoy!!")
            # TODO: 7. Make Coffee

            else:
                print("Sorry that's not enough money. Money refunded!")
