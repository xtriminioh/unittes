import unittest
from product import Product

class TestShoppingCart(unittest.TestCase):

    def test_product_object(self):
        name = 'Manzana'
        price = 1.70

        new_product = Product(name,price)

        #verificamos si los atributos que se crearon los tiene el nuevo producto
        self.assertEqual(new_product.name, name, 'Lo sentimos, el nombre no es el mismo.')
        self.assertEqual(new_product.price, price, 'Lo sentimos, el precio no es el mismo.')


if __name__ == '__main__': unittest.main()