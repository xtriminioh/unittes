import pytest

#En pytest, se puede realizar las pruebas unitarias,
#mediante funciones las cuales tienen que tener el prefijo
#[test_<nombre_de_la_funcion>] y dentro de la funcion vamos
#a condicionar con la palabra reservada assert ya que esta 
#lanza un error en caso que la condicion no se cumpla.

def test_example():
    assert 10 == 10