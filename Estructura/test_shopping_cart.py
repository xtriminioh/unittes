import unittest
from product import Product

class TestShoppingCart(unittest.TestCase):

    #Metodos setup y teardown de TestCase
    def setUp(self):
        """"El metodo setUp se ejecuta antes de cada unas de las puebas."""
        self.name = 'iPhone'
        self.price = 500.00
        self.smartphone = Product(self.name,self.price)

    def tearDown(self):
        """"El metodo tearDown se ejecuta despues de cada unas de las puebas."""
        pass

    def test_product_object(self):
        name = 'Manzana'
        price = 1.70

        new_product = Product(name,price)

        #verificamos si los atributos que se crearon los tiene el nuevo producto
        self.assertEqual(new_product.name, name, 'Lo sentimos, el nombre no es el mismo.')
        self.assertEqual(new_product.price, price, 'Lo sentimos, el precio no es el mismo.')

    def test_product_name(self):
        self.assertEqual(self.smartphone.name,self.name, 'Lo sentimos, el nombre del producto no es el mismo.') 

if __name__ == '__main__': unittest.main()