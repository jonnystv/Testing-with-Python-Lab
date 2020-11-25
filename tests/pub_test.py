#tests/pub_test.py

import unittest
from src.pub import Pub
from src.drink import Drink 
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("beer", 4)
        self.drink_2 = Drink("wine", 5)

        self.drinks = [self.drink_1, self.drink_2]
        self.pub = Pub("The Prancing Pony", 100, self.drinks)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)


    def test_pub_has_drink(self):
        self.assertEqual(2, len(self.drinks))
    
    def test_pub_takes_payment(self):
        self.pub.takes_payment(self.drink_1)
        self.assertEqual(104, self.pub.money)

    def test_pub_gives_drink(self):
        self.pub.gives_drink(self.drink_1)
        self.assertEqual(1, len(self.drinks))