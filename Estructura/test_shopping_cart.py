import unittest

from product import Product
from product import ProductDiscountError
from shopping_cart import ShoppingCart

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
        self.shopping_cart_1 = ShoppingCart()

        self.shopping_cart_2 = ShoppingCart()
        self.shopping_cart_2.add_product(self.smartphone)


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

    def test_shopping_cart_empty(self):
        self.assertTrue(
            self.shopping_cart_1.empty(),
            'Lo sentimos, el carrito de compra esta vacio!'
        )

    def test_shopping_cart_has_product(self):
        self.assertTrue(self.shopping_cart_2.has_products())
        self.assertFalse(self.shopping_cart_2.empty())

    def test_product_in_shopping_cart(self):
        self.assertIn(self.smartphone, self.shopping_cart_2.products)
    
    def test_product_not_in_shopping_cart(self):
        self.shopping_cart_2.remove_product(self.smartphone)
        self.assertNotIn(self.smartphone, self.shopping_cart_2.products)

    def test_discount_error(self):
        """En este contexto, realizaremos las operaciones 
            que nos lanzaran el error"""
        with self.assertRaises(ProductDiscountError):
            Product(name='Example',price=10.0, discount=11.0)

if __name__ == '__main__': unittest.main()