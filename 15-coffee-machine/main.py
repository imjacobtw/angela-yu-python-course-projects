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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")


def has_sufficient_ingredients(menu_item):
    for ingredient, amount in MENU[menu_item]["ingredients"].items():
        if amount > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False

    return True


def get_payment():
    total = 0
    total += 0.25 * int(input("How many quarters? "))
    total += 0.10 * int(input("How many dimes? "))
    total += 0.05 * int(input("How many nickels? "))
    total += 0.01 * int(input("How many pennies? "))
    return total


def update_resources(menu_item):
    menu_item_cost = MENU[menu_item]["cost"]
    resources["money"] += menu_item_cost

    for resource in resources:
        ingredients_dict = MENU[menu_item]["ingredients"]
        if resource in ingredients_dict:
            resources[resource] -= ingredients_dict[resource]


is_using_machine = True

while is_using_machine:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "off":
        is_using_machine = False
    elif user_input == "report":
        print_report()
    elif user_input not in MENU:
        print("That is not a valid menu item. Please try again.")
    else:
        menu_item = user_input
        menu_item_cost = MENU[menu_item]["cost"]

        if has_sufficient_ingredients(menu_item):
            print("Please insert coins.")
            money_inserted = get_payment()

            if money_inserted >= menu_item_cost:
                change = money_inserted - menu_item_cost
                update_resources(menu_item)

                print(f"Here is ${change:.2f} in change.")
                print(f"Here is your {menu_item} ☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
