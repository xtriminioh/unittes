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

class TestExmaple():
    def test_suma_dos_numeros(self):
        assert 10 + 10 == 20, 'Lo sentimos, la suma no es correcta!'

    def test_resta_dos_numeros(self):
        assert 10 - 10 == 20, 'Lo sentimos, la resta no es correcta!'