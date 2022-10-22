import unittest

from entities.product import Product
from entities.product import ProductDiscountError
from entities.shopping_cart import ShoppingCart

#Mensages para los diferentes [skip] metodos
skip_msg = 'La prueba no cumple con los requerimientos necesarios.'
skipIF_msg = 'No se cuenta con todos los requerimientos.'
skipUnLess_msg = 'No se cuenta con todos los requerimientos.'

#funcion para verificar en true para el metodo [skipIf] 
def is_available_to_skip():
    """En esta funcion se puede realizar las diferentes comprobaciones.
        para detectar si se puede realizar un prueba unitaria.
    """
    return True

#funcion para verificar en false para el metodo [skipUnless] 
def is_connected():
    """Es esta funcion se puere realizar el test si se realizado.
        una conexion a una base de datos. para de esta forma relizar
        la prueba unitaria.
    """
    return False


#TestCase contiene todo los metodos de assert para los diferentes
#casos de testeo.
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
        pass

    def tearDown(self):
        """Este Metodo teardown se ejeuta despues de cada una de las pruebas."""
        pass

    def test_shopping_cart_empty(self):
        msg_error = 'Lo sentimos, el carrito de compra esta vacio!'
        self.assertTrue(self.shopping_cart_1.empty(), msg_error)

    def test_shopping_cart_has_product(self):
        self.assertTrue(self.shopping_cart_2.has_products())
        self.assertFalse(self.shopping_cart_2.empty())

    def test_product_in_shopping_cart(self):
        self.assertIn(self.smartphone, self.shopping_cart_2.products)
    
    def test_product_not_in_shopping_cart(self):
        self.shopping_cart_2.remove_product(self.smartphone)
        self.assertNotIn(self.smartphone, self.shopping_cart_2.products)


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

    #Formas de saltar, las pruebas unitarias. (Que las pruebas no se ejecuten)
    #En unittest, 
    #(1) - cuando el desarrollador, conoce de ante mano que la pueba no puede ejecutarce, 
    #(2) - cuando el desarrollador, desconoce su la prueba puede o no ejecutarse.
    #pricipalmente debido a factores externos.

    #caso (1)
    @unittest.skip(skip_msg)
    def test_skip_example(self):
        #Esta prueba sera saltada, y para ello utiliza el decorador @unittest.skip()
        #el cual recibe un string.
        self.assertEqual(1,1)

    #caso (2)
    # skipIf -> Evalua sobre Verdadero
    # skipUnless -> Evalua sobre Falso.
    @unittest.skipIf(is_available_to_skip(), skipIF_msg)
    def test_skip_example_two(self):
        #Esta prueba sera saltada solo si se cumple una condicion booleana, [Evalua sobre Verdadero]
        #y para ello utiliza el decorador @unittest.skipIf(arg1,arg2)
        #donde el primero arg1 -> puede ser una funcion que retorne un boolean
        #y el segundo arg2 -> sera un string con un msjs para el usuario.
        pass

    @unittest.skipUnless(is_connected(), skipUnLess_msg)
    def test_skip_example_three(self):
        #Esta prueba sera saltada solo si se cumple una condicion booleana, [Evalua sobre Falso]
        #y para ello utiliza el decorador @unittest.skipUnless(arg1,arg2)
        #donde el primero arg1 -> puede ser una funcion que retorne un boolean
        #y el segundo arg2 -> sera un string con un msjs para el usuario.
        pass

