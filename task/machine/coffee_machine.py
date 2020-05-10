class CoffeeMachine:
    espresso_resources = {"water": 250, "coffee beans": 16, "cups": 1, "money": -4, "milk": 0}
    latte_resources = {"water": 350, "milk": 75, "coffee beans": 20, "cups": 1, "money": -7}
    cappuccino_resources = {"water": 200, "milk": 100, "coffee beans": 12, "cups": 1, "money": -6}

    def __init__(self):
        self.action = None
        self.state = "choosing an action"
        self.resources = {"water": 400, "milk": 540, "coffee beans": 120, "cups": 9, "money": 550}

    def machine_info(self):
        print("The coffee machine has:")
        print(str(self.resources["water"]) + " of water")
        print(str(self.resources["milk"]) + " of milk")
        print(str(self.resources["coffee beans"]) + " of coffee beans")
        print(str(self.resources["cups"]) + " of disposable cups")
        print("$" + str(self.resources["money"]) + " of money\n")

    def is_enough_resources(self):
        self.state = "choosing an action"
        if self.action == "1":
            for key in self.espresso_resources.keys():
                if self.resources[key] < self.espresso_resources[key]:
                    print("Sorry, not enough {}\n!".format(key))
                    return False
        elif self.action == "2":
            for key in self.latte_resources.keys():
                if self.resources[key] < self.latte_resources[key]:
                    print("Sorry, not enough {}\n!".format(key))
                    return False
        elif self.action == "3":
            for key in self.cappuccino_resources.keys():
                if self.resources[key] < self.cappuccino_resources[key]:
                    print("Sorry, not enough {}\n!".format(key))
                    return False

        return True

    def fill_machine(self):
        self.resources["water"] += int(input("Write how many ml of water do you want to add:\n> "))
        self.resources["milk"] += int(input("Write how many ml of milk do you want to add:\n> "))
        self.resources["coffee beans"] += int(input("Write how many grams of coffee beans do you want to add:\n> "))
        self.resources["cups"] += int(input("Write how many disposable cups of coffee do you want to add:\n> "))
        print()

    def gave_money(self):
        print("I gave you $" + str(self.resources["money"]))
        print()
        self.resources["money"] = 0

    def make_coffee(self):
        if self.is_enough_resources():
            if self.action == "1":
                for key in self.espresso_resources.keys():
                    self.resources[key] -= self.espresso_resources[key]
            elif self.action == "2":
                for key in self.latte_resources.keys():
                    self.resources[key] -= self.latte_resources[key]
            elif self.action == "3":
                for key in self.cappuccino_resources.keys():
                    self.resources[key] -= self.cappuccino_resources[key]

            print("I have enough resources, making you a coffee!\n")

            self.state = "choosing an action"

        self.action = "back"

    def buy_coffee(self):
        while self.action != "back" or self.state == "choosing a type of coffee":
            self.action = input("What do you want to buy?"
                                " 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n> ")

            self.make_coffee()

    def input(self):
        while self.action != "exit":
            if self.state == "choosing an action":
                print("Write action (buy, fill, take, remaining, exit):")
                self.action = input("> ")
                print()

                if self.action == "remaining":
                    self.machine_info()
                elif self.action == "fill":
                    self.fill_machine()
                elif self.action == "take":
                    self.gave_money()
                elif self.action == "buy":
                    self.state = "choosing a type of coffee"
                    self.buy_coffee()
