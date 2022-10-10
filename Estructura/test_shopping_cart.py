import unittest
from product import Product

class TestShoppingCart(unittest.TestCase):

    def test_product_object(self):
        name = 'Manzana'
        price = 1.70

        self.new_product = Product(name,price)

        #verificamos si los atributos que se crearon los tiene el nuevo producto
        self.assertEqual(self.new_product.name, name)
        self.assertEqual(self.new_product.price, price)


if __name__ == '__main__':
    unittest.main()