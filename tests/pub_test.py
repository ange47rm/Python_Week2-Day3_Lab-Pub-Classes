import unittest

from src.pub import Pub 
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp (self):
        self.pub = Pub("The Prancing Pony", 100.00)

    
    def test_pub_has_name(self):
        self.assertEqual ("The Prancing Pony", self.pub.name)

    
    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_has_drinks(self):
        drink_1 = Drink("Coke", 3)
        drink_2 = Drink("Beer", 5)
        self.pub.drinks.append(drink_1)
        self.pub.drinks.append(drink_2)
        self.assertEqual(2, len(self.pub.drinks))

    def test_sale_of_drink(self):
        drink_2 = Drink("Beer", 5)
        self.assertEqual (105.00, self.pub.sell_drink(drink_2))
        

    











    # def test_pub(self):
    #     # arrange
    #     person = Person ()
    #     # act
    #     pub.get_till_total()
    #     pub.kick_out_guest()
    #     # assert
    #     self.assertEqual