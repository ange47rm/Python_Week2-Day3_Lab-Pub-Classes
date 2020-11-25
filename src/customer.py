class Customer():
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet


    def buy_drink(self, drink, pub):

        if self.wallet >= drink.price:
            self.wallet -= drink.price
            pub.till += drink.price
            return self.wallet

        else:
            return "Customer has not enough money"

