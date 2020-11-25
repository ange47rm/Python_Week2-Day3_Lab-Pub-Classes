class Pub():
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        
    def sell_drink(self, drink, customer):
        if customer.age >= 18 and customer.drunkenness <= 8:
            self.till += drink.price    
            return self.till 

        else:
            return "Customer cannot buy drink"

