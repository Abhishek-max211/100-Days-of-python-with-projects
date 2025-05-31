# Project-16 = The Coffee Machine in OOP
print('''
⠀⠀⠀⠀⠀⠀⢀⡴⠁⠀⠀⣠⠎⠀⠀⠀⣴⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⣧⡀⠀⢰⣿⣄⠀⠀⣾⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠻⣿⣷⡌⠛⢿⣿⣦⠈⠛⢿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡸⠟⠀⠀⢀⠿⠃⠀⠀⠀⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣀⣀⣈⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠿⣷⣦⡀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠈⠻⣷⡀⠀⠀
⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⣿⡇⠀⠀
⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⣀⣾⡿⠁⠀⠀
⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣸⣿⣿⠿⠛⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠠⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀
''')
class MenuItem:
    def __init__(self, name, ingredients, cost):
        self.name = name
        self.ingredients = ingredients
        self.cost = cost


class Menu:
    def __init__(self):
        self.items = {
            "espresso": MenuItem("espresso", {"water": 50, "coffee": 10}, 1.5),
            "latte": MenuItem("latte", {"water": 200, "milk": 150, "coffee": 24}, 2.5),
            "cappuccino": MenuItem("cappuccino", {"water": 250, "milk": 100, "coffee": 24}, 3.0)
        }

    def get_items(self):
        return "/".join(self.items.keys())

    def find_drink(self, name):
        return self.items.get(name, None)


class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources.get(item, 0):
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_coffee(self, drink):
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]
        print(f"Here is your {drink.name} ☕️. Enjoy!")


class MoneyMachine:
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0

    def report(self):
        print(f"Money: ${self.profit:.2f}")

    def process_coins(self):
        print("Please insert coins.")
        total = 0
        try:
            for coin, value in self.COIN_VALUES.items():
                count = int(input(f"How many {coin}? "))
                total += count * value
        except ValueError:
            print("Invalid input.")
            return 0
        return round(total, 2)

    def make_payment(self, cost):
        amount = self.process_coins()
        if amount >= cost:
            change = round(amount - cost, 2)
            print(f"Here is ${change:.2f} in change.")
            self.profit += cost
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False


def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    is_on = True
    while is_on:
        choice = input(f"\nWhat would you like? ({menu.get_items()}): ").lower()
        if choice == "off":
            print("Shutting down. Goodbye!")
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if drink:
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)
            else:
                print("Invalid choice. Please choose a valid drink.")


if __name__ == "__main__":
    main()
