import unittest

from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink_1 = Drink("Coke", 3)
        self.drink_2 = Drink("Beer", 5)

    def test_drink_has_name(self):
        self.assertEqual ("Coke", self.drink_1.name)

    def test_drink_has_price(self):
        self.assertEqual (3, self.drink_1.price)

