import pytest

#En pytest, se puede realizar las pruebas unitarias,
#mediante funciones las cuales tienen que tener el prefijo
#[test_<nombre_de_la_funcion>] y dentro de la funcion vamos
#a condicionar con la palabra reservada assert ya que esta 
#lanza un error en caso que la condicion no se cumpla.

def test_example():
    assert 10 == 10

#realiar puebas unitarias mediante la implementacion de las clases
#se utilizar la siguiente nomenclatura [class Test<nombre_de_la_clase>()]
#y esta no hereda de otra. y dentro de la clase utilizarimos metodos
#que inicien con [test_<nombre_del_metodo>]

class TestExample():

    @classmethod
    def setup_class(cls):
        """Este metodo a nivel de clase, se ejecuta antes de todas las pruebas"""
        pass

    @classmethod
    def teardown_class(cls):
        """Este metodo a nivel de clase, se ejecuta desues de todas las pruebas"""
        pass

    def setup_method(self):
        """Este metodo se ejecutara antes de cada prueba"""
        print('>> method setup')

    def teardown_method(self):
        """Este metodo se ejecutara despues de cada prueba"""
        print('>> method teardown')

    def test_suma_dos_numeros(self):
        mgs = 'Lo sentimos, la suma no es correcta!'
        assert 10 + 10 == 20, mgs 

    def test_resta_dos_numeros(self):
        mgs = 'Lo sentimos, la resta no es correcta!'
        assert 10 - 10 == 0, msg

class TestExample2():
    def test_multiplicacion_dos__numeros(self):
        mgs = 'Lo sentimos, la multiplicacion no es correcta!'
        assert 2 * 10 == 20, msg 
