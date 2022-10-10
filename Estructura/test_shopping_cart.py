import unittest
from product import Product

class TestShoppingCart(unittest.TestCase):

    def test_product_object(self):
        name = 'Manzana'
        price = 1.70

        self.new_product = Product(name,price)
