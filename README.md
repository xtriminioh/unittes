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

example:  
=> python -m pip install pytest  

Para ejecutar la libreria de pytest, simplente con el entorno activado, ejecutamos:  

example:  
=> pytest  

### Como utilizar la libreria Pytest
Despues de tener instalado la libreria de Pytest, (en el entorno virual).  
Solo lo ejecutamos con el comando:  

example:  
=> pytest  

Para que este pueda ejecutar todas los test que contenga la carpeta  
de conde fue ejecutado. Y se puede realizar varias formas, ya sea por  
medio de funciones y por medio de clases.  

1) - Para utilizar por medio de las funciones se realizar de la siguientes manera:  

example:  
=>  def test_<nombre_de_la_funcion>():  
        assert <condicion_a_evaluar>,<mensaje_del_error>  

2) - Para utilziar por medio de las clases se realizar de la siguiente manera:  
     esta clase no require adquirir una herrencia.  

example:  
=>  class Test<Example>():  
        def test_<nombre_del_metodo>(self):  
            assert <condicion_a_evaluar>,<mensaje_del_error>  

Al trabajar con clases para realizar las pruebas unitarias, podremos ejecutar una prueba en  
especifico. y tambien podremos ver el estado de las prueba con las bandera [-v]  
Estos para llevar a cabo la ejecucion de una prueba en especifico.

example:  
=>  pytest <nombre_del_modulo>::<nombre_de_la_clase>::<nombre_del_metodo> -v  


### Metodos Setup y Teardown en la libreria Pytest

example:  
=> setup_method(self):  
        se ejecuta antes de cada prueba.  


example:  
=> teardown_method(self):  
        se ejecuta despues de cada prueba.  

Estos metodos se ejecutan a nivel de clase  
y estos tiene que llevar un decorador: @classmethod  
y resiven como parametro cls  

example:  
   @classmethod  
=> setup_class(cls):  
        se ejecuta antes de todas las pruebas  

example:  
   @classmethod  
=> teardown_class(cls):  
        se ejecuta despues de todas las pruebas  

### Metodos de Etiquetado de la libreria Pytest  
Una prueba puede tener multiples etiquetas o multiples marcas  
Y una etiqueta puede estar en multiples pruebas.  

Es por medio de estas marcar que podemos categorizar que pruebas  
deseamos realiar.

Para agregar una marca a una prueba solamente tenemos que decorarla  
de la siguiete forma.

example:  
=>  @pytest.mark.<nombre_etiqueta>  
    def test_<nombre_prueba>:  
        pass  

Para ejecutar solamente las marcas o etiquetas que deseamos  
lo podemos hacer con el flag -m <nombre_etiqueta>  

example:  
=> pytest <nombre_del_documento.py> -v -m <etiqueta>  


### Etiquetas skip y skipif  
Para hacer uso de este tipo de etiquetas lo unico que tenemos que hacer  
es agregar un decorador a la metodo test al cual queremos saltar  
con un parametro (reason='<mensaje>') para dar a conocer porque se esta  
saltando el metodo decorado.

example:  
=>  @pytest.mark.skip(reason='<mensage>')  
    def test_skip():  
        pass  

Tambien contamos con la etiqueta skipif el cual evalua sobre verdadero,  
lo que quiere decir que si la condicion evaluada es [True] esta prueba  
sera saltada pero si de lo contrario la condicion evaluada es [False]  
la prueba se ejecutara con normalidad.


example:  
=>  @pytest.mark.skipif(condition , reason='<mensage>')  
    def test_skipif():  
        pass  


### Proveer Datos a Pruebas (fixture)
Las fixtures son funciones que se ejecutan antes de todas las pruebas y  
tienen como objetivo proveer de ciertos parametros a las pruebas.  

Las fixtures se utilizan para pasarles parametros las pruebas unitarias  
que se implementan por medio de funciones, y para llevar a cabo esto  
primero tenemos que crear un funcion que lleve como nombre el  
mismo nombre del parametro que deseamos pasar a la funcion de prueba.  
y esta tiene que esta decorada [@pytest.fixture] para que pytest reconoca  
como un proveedor de Datos para un prueba en especifico.  

example:  
=>  @pytest.fixture
    def username():  
        return 'Cody'  

=>  def test_username(username):  
        assert username == 'Cody'  


### Modificaciones de las fixture
Con la palabra reservada [yield] la cual permite pausar momentaneamente  
la ejecución de la funcion cuando el bloque de codigo que llamo a la  
finalize, reanudara sus actividades.  

Por lanto utilizando [yield] seremos capases de ejecutar acciones  
Antes o Despues de las pruebas.

example:  
=>  @pytest.fixture  
    def username():  
        yield '<username>'  

nota: La utilizacion de yield en las pruebas unitarias mediantes  
      metodos de funciones, es para simular la [setup] y [teardown]  
      que tiene las clases y los metodos de las clases.  
