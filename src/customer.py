from src.pub import Pub
#import pdb 

class Customer():

    def __init__(self, name, wallet):
        self.name = name 
        self.wallet = wallet
        self.drinks = []
    
    
    def pay_for_drink(self, drink):
        self.wallet -= drink.price

    def receives_drink(self, drink):
        self.drinks.append(drink)

    def buys_drink(self, drink, pub):
        # pdb.set_trace()
        if self.wallet >= drink.price:
            self.receives_drink(drink)
            pub.gives_drink(drink)
            self.pay_for_drink(drink)
            pub.takes_payment(drink)

    