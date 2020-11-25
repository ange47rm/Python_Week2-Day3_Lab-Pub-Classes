class Customer():
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age


    def buy_drink(self, drink, pub):

        if self.wallet >= drink.price:
            self.wallet -= drink.price
            pub.till += drink.price
            return self.wallet

        else:
            return "Customer has not enough money"

