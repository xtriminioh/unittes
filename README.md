# unittes
En este repositorio, esta hecho para llevar los apuntes, del curso de codigo facilito.  
De las Pruebas Unitarias

### Estructura de Proyectos
En las estructura de los proyectoS, en los cuales se podra trabajar, por medio de la
creacion de modulos, y realizando algunas pruebas con las librerias que nos facilita
el mismo lenguaje de programacion de Python.

En la estructura del entities la cual es la carpeta que contiene los script de la
logica, en esta se tiene que incluir un archivo con el nombre de [__init__.py] en
donde estaran espuestos, las diferentes clases que sean pertenecientes al modulo
en cuestion. Y agregamos dentro de la carpeta (entities) todos los archivos (script)
que son pertenencientes al modulo completo.

Luego se crea un archivo main, del cual se realiza la importacion del modulo con el 
siguientes formato:

example:
=> from [nombre_modulo] import [nombre_clase]

### Libreria de Pytest
creamos una nueva carpeta, con el nombre Libreria_Pytest para ahi tener que ir colocando
las diferentes pruebas que realizaremos con la libreria Pytest.
realizamos la instalacion de la libreria de pytest, pero no sin antes crear un entorno
virtual, en mi caso con Conda. Y luego de tener ya creado y activiado el entorno virtual
ejecutamos el siguiente comando:

=> python -m pip install pytest

Para ejecutar la libreria de pytest, simplente con el entorno activado, ejecutamos:

=> pytest

### Como utilizar la libreria Pytest
Despues de tener instalado la libreria de Pytest, (en el entorno virual).
Solo lo ejecutamos con el comando:

=> pytest

Para que este pueda ejecutar todas los test que contenga la carpeta
de conde fue ejecutado. Y se puede realizar varias formas, ya sea por
medio de funciones y por medio de clases.

1) - Para utilizar por medio de las funciones se realizar de la siguientes manera:
=>  def test_<nombre_de_la_funcion>():
        assert <condicion_a_evaluar>,<mensaje_del_error>

2) - Para utilziar por medio de las clases se realizar de la siguiente manera:
     esta clase no require adquirir una herrencia.
=>  class Test<Example>():
        def test_<nombre_del_metodo>(self):
            assert <condicion_a_evaluar>,<mensaje_del_error>

Al trabajar con clases para realizar las pruebas unitarias, podremos ejecutar una prueba en
especifico. y tambien podremos ver el estado de las prueba con las bandera [-v]
Estos para llevar a cabo la ejecucion de una prueba en especifico.

=>  pytest <nombre_del_modulo>::<nombre_de_la_clase>::<nombre_del_metodo> -v


