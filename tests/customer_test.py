import unittest 

from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer_1 = Customer("Tim", 30.00, 20)
        self.customer_2 = Customer("Jane", 4.00, 16)

    def test_customer_has_name(self):
        self.assertEqual ('Tim', self.customer_1.name)

    
    def test_customer_has_wallet(self):
        self.assertEqual (30.00, self.customer_1.wallet)

    def test_customer_can_buy_drink(self):
        drink_1 = Drink("Coke", 3, 0)
        pub = Pub("The Prancing Pony", 100.00)
        self.assertEqual ((1.0, 0), self.customer_2.buy_drink_and_increase_drunkenness(drink_1, pub))
        
    def test_customer_cannot_buy_drink(self):
        drink_2 = Drink("Beer", 5, 4)
        pub = Pub("The Prancing Pony", 100.00)
        self.assertEqual("Customer has not enough money", self.customer_2.buy_drink_and_increase_drunkenness(drink_2, pub))

    def test_drunkenness_increase(self):
        drink_2 = Drink("Beer", 5, 4)
        pub = Pub("The Prancing Pony", 100.00)
        self.assertEqual((25.0, 4), self.customer_1.buy_drink_and_increase_drunkenness(drink_2, pub))
        