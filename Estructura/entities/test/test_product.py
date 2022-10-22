import unittest

from entities.product import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        """Este metodo setup se ejecuta antes que todas las demas pruebas"""
        self.name = 'iPhone'
        self.price = 500.00

        self.smartphone = Product(self.name, self.price)
        self.shopping_cart_1 = ShoppingCart()

        self.shopping_cart_2 = ShoppingCart()
        self.shopping_cart_2.add_product(self.smartphone)

    def test_product_object(self):
        name = 'Manzana'
        price = 1.70

        new_product = Product(name,price)

        #verificamos si los atributos que se crearon los tiene el nuevo producto
        self.assertEqual(new_product.name, name)
        self.assertEqual(new_product.price, price)

    def test_product_name(self):
        self.assertEqual(self.smartphone.name, self.name)

    def test_product_price(self):
        self.assertEqual(self.smartphone.price, self.price)

    def test_discount_error(self):
        #En este contexto, realizaremos las operaciones 
        #que nos lanzaran el error.
        with self.assertRaises(ProductDiscountError):
            Product(name='Example',price=10.0, discount=11.0)

    #Validar expresiones regulares con assertRegex
    def test_code_product(self):
        msg_error = 'la expresion, Lo sentimos, el codigo no cumple con la expresion'
        self.assertRegex(self.smartphone.code, self.smartphone.name, msg_error)