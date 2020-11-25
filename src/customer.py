class Customer():
    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness


    def buy_drink_and_increase_drunkenness(self, drink, pub):

        if self.wallet >= drink.price:
            self.wallet -= drink.price
            self.drunkenness += drink.alcohol_level
            return self.wallet, self.drunkenness

        else:
            return "Customer cannot buy drink"


