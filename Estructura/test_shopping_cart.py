import unittest
from product import Product

class TestShoppingCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Este Metodo setUpClass son metodos de clase y se ejecuta antes
            de todas las pruebas - decorar @classmethod"""
        pass

    @classmethod
    def tearDownClass(cls):
        """Este Metodo tearDownClass son metodos de clase y se ejecuta despues 
            de todas las pruebas - decorar @classmethod"""
        pass

    def setUp(self):
        """Este Metodo setup se ejecuta antes de cada una de las pruebas."""
        self.name = 'iPhone'
        self.price = 500.00

        self.smartphone = Product(self.name, self.price)


    def tearDown(self):
        """Este Metodo teardown se ejeuta despues de cada una de ls pruebas."""
        pass

    def test_product_object(self):
        name = 'Manzana'
        price = 1.70

        new_product = Product(name,price)

        #verificamos si los atributos que se crearon los tiene el nuevo producto
        self.assertEqual(new_product.name, name)
        self.assertEqual(new_product.price, price)

    def test_prrduct_name(self):
        self.assertEqual(self.smartphone.name, self.name)

    def test_prrduct_price(self):
        self.assertEqual(self.smartphone.price, self.price)

if __name__ == '__main__':
    unittest.main()