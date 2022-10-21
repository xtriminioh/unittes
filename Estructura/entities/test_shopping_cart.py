import unittest

from entities.product import Product
from entities.product import ProductDiscountError
from entities.shopping_cart import ShoppingCart

def is_available_to_skip():
    """En esta funcion se puede realizar las diferentes comprobaciones.
        para detectar si se puede realizar un prueba unitaria.
    """
    return True

def is_connected():
    """Es esta funcion se puere realizar el test si se realizado.
        una conexion a una base de datos. para de esta forma relizar
        la prueba unitaria.
    """
    return False

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

    def test_product_name(self):
        self.assertEqual(self.smartphone.name, self.name)

    def test_product_price(self):
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
        #En este contexto, realizaremos las operaciones 
        #que nos lanzaran el error.
        with self.assertRaises(ProductDiscountError):
            Product(name='Example',price=10.0, discount=11.0)

    def test_total_shopping_cart(self):
        #creamos nuevos productos y los agregados al carrito de compra.
        self.shopping_cart_1.add_product(Product(name='Libro', price=15.0))
        self.shopping_cart_1.add_product(Product(name='Camara', price=700.0, discount=70.0))

        #assertGreater nos permite evaluar mayor que.
        self.assertGreater(self.shopping_cart_1.total,0)
        #assertLess nos permite evaluar menor que.
        self.assertLess(self.shopping_cart_1.total,1000)
        #assertEqual nos permite evaluar a igual
        self.assertEqual(self.shopping_cart_1.total,645.00)
        #assertGreaterEqual es igual que >=
        #assertLessEqual es igual que <=

    def test_total_empty_shopping_cart(self):
        self.assertEqual(self.shopping_cart_1.total, 0)

    #Formas de saltar, las pruebas unitarias. (Que las puebas no se ejecuten)
    #En unittest, (1) - cuando el desarrollador, conoce de ante mano que la pueba no
    #puede ejecutarce, (2) - cuando el desarrollador, desconoce su la prueba puede
    #o no ejecutarse.
    # pricipalmente debido a factores externos.

    #caso (1)
    @unittest.skip('La prueba no cumple con los requerimientos necesarios.')
    def test_skip_example(self):
        #Esta prueba sera saltada, y para ello utiliza el decorador @unittest.skip()
        #el cual recibe un string.
        self.assertEqual(1,1)

    #caso (2)
    # skipIf -> Evalua sobre Verdadero
    # skipUnless -> Evalua sobre Falso.
    @unittest.skipIf(is_available_to_skip(),'No se cuenta con todos los requerimientos.')
    def test_skip_example_two(self):
        pass

    @unittest.skipUnless(is_connected(),'No se cuenta con todos los requerimientos.')
    def test_skip_example_three(self):
        pass

    #Validar expresiones regulares con assertRegex
    def test_code_product(self):
        self.assertRegex(
            self.smartphone.code,
            self.smartphone.name,
            'la expresion, Lo sentimos, el codigo no cumple con la expresion'
        )

if __name__ == '__main__':
    unittest.main()