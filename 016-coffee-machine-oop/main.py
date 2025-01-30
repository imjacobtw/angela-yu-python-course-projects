from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_using_machine = True
the_menu = Menu()
the_coffee_maker = CoffeeMaker()
the_money_machine = MoneyMachine()

while is_using_machine:
    user_input = input(f"What would you like? ({the_menu.get_items()}): ")

    if user_input == "off":
        is_using_machine = False
    elif user_input == "report":
        the_coffee_maker.report()
        the_money_machine.report()
    else:
        drink = the_menu.find_drink(user_input)

        if (
            drink
            and the_coffee_maker.is_resource_sufficient(drink)
            and the_money_machine.make_payment(drink.cost)
        ):
            the_coffee_maker.make_coffee(drink)
