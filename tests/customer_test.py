import unittest

from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestCustomer(unittest.TestCase):
  def setUp(self):
    self.customer = Customer("Dan", 20.00)

  def test_customer_has_name(self):
    self.assertEqual("Dan", self.customer.name)

  def test_customer_has_wallet(self):
    self.assertEqual(20.00, self.customer.wallet)