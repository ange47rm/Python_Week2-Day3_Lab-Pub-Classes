import unittest 

from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer_1 = Customer("Tim", 30.00)
        self.customer_2 = Customer("Jane", 4.00)

    def test_customer_has_name(self):
        self.assertEqual ('Tim', self.customer_1.name)

    
    def test_customer_has_wallet(self):
        self.assertEqual (30.00, self.customer_1.wallet)

    def test_customer_can_buy_drink(self):
        drink_1 = Drink("Coke", 3)
        self.assertEqual (1.00, self.customer_2.buy_drink(drink_1))
        
    def test_customer_cannot_buy_drik(self):
        drink_2 = Drink("Beer", 5)
        self.assertEqual("Customer has not enough money", self.customer_2.buy_drink(drink_2))
