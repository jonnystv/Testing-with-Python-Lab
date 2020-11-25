class Pub():
    def __init__(self, name, money, drinks):
        self.name = name
        self.money = money
        self.drinks = drinks


    def takes_payment(self, drink):
        self.money += drink.price

    def gives_drink(self, drink):
        self.drinks.remove(drink)