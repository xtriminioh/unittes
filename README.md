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
```python
        from [nombre_modulo] import [nombre_clase]  
```

### Libreria de Pytest
creamos una nueva carpeta, con el nombre Libreria_Pytest para ahi tener que ir colocando
las diferentes pruebas que realizaremos con la libreria Pytest.
realizamos la instalacion de la libreria de pytest, pero no sin antes crear un entorno
virtual, en mi caso con Conda. Y luego de tener ya creado y activiado el entorno virtual
ejecutamos el siguiente comando:  

example:  
```python
        python -m pip install pytest
```

Para ejecutar la libreria de pytest, simplente con el entorno activado, ejecutamos:  

example:  

```python
        pytest  
```

### Como utilizar la libreria Pytest
Despues de tener instalado la libreria de Pytest, (en el entorno virual).  
Solo lo ejecutamos con el comando:  

example:  

```python
        pytest  
```

Para que este pueda ejecutar todas los test que contenga la carpeta  
de conde fue ejecutado. Y se puede realizar varias formas, ya sea por  
medio de funciones y por medio de clases.  

1) - Para utilizar por medio de las funciones se realizar de la siguientes manera:  

example:  

```python
        def test_<nombre_de_la_funcion>():  
                assert <condicion_a_evaluar>,<mensaje_del_error>  
```

2) - Para utilziar por medio de las clases se realizar de la siguiente manera:  
     esta clase no require adquirir una herrencia.  

example:  

```python
        class Test<Example>():  
                def test_<nombre_del_metodo>(self):  
                        assert <condicion_a_evaluar>,<mensaje_del_error>  
```

Al trabajar con clases para realizar las pruebas unitarias, podremos ejecutar una prueba en  
especifico. y tambien podremos ver el estado de las prueba con las bandera [-v]  
Estos para llevar a cabo la ejecucion de una prueba en especifico.

example:  

```python
        pytest <nombre_del_modulo>::<nombre_de_la_clase>::<nombre_del_metodo> -v  
```

### Metodos Setup y Teardown en la libreria Pytest

example:  

```python
        def setup_method(self):  
        #se ejecuta antes de cada prueba.  
```

example:  
```python
        def teardown_method(self):  
        #se ejecuta despues de cada prueba.  
```

Estos metodos se ejecutan a nivel de clase  
y estos tiene que llevar un decorador: @classmethod  
y resiven como parametro cls  

example:  

```python
        @classmethod  
        def setup_class(cls):
        #se ejecuta antes de todas las pruebas  
```

example:  

```python
        @classmethod  
        def teardown_class(cls):  
        #se ejecuta despues de todas las pruebas  
```

### Metodos de Etiquetado de la libreria Pytest  
Una prueba puede tener multiples etiquetas o multiples marcas  
Y una etiqueta puede estar en multiples pruebas.  

Es por medio de estas marcar que podemos categorizar que pruebas  
deseamos realiar.

Para agregar una marca a una prueba solamente tenemos que decorarla  
de la siguiete forma.

example:  

```python
        @pytest.mark.<nombre_etiqueta>  
        def test_<nombre_prueba>:  
                pass  
```

Para ejecutar solamente las marcas o etiquetas que deseamos  
lo podemos hacer con el flag -m <nombre_etiqueta>  

example:  
```python
        pytest <nombre_del_documento.py> -v -m <etiqueta>  
```

### Etiquetas skip y skipif  
Para hacer uso de este tipo de etiquetas lo unico que tenemos que hacer  
es agregar un decorador a la metodo test al cual queremos saltar  
con un parametro (reason='<mensaje>') para dar a conocer porque se esta  
saltando el metodo decorado.

example:  

```python
    @pytest.mark.skip(reason='<mensage>')  
    def test_skip():  
        pass
```

Tambien contamos con la etiqueta skipif el cual evalua sobre verdadero,  
lo que quiere decir que si la condicion evaluada es [True] esta prueba  
sera saltada pero si de lo contrario la condicion evaluada es [False]  
la prueba se ejecutara con normalidad.


example:  

```python
    @pytest.mark.skipif(condition , reason='<mensage>')  
    def test_skipif():  
        pass
```

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
```python
    @pytest.fixture
    def username():  
        return 'Cody'  

    def test_username(username):  
        assert username == 'Cody'  
```

### Modificaciones de las fixture
Con la palabra reservada [yield] la cual permite pausar momentaneamente  
la ejecuci??n de la funcion cuando el bloque de codigo que llamo a la  
finalize, reanudara sus actividades.  

Por lanto utilizando [yield] seremos capases de ejecutar acciones  
Antes o Despues de las pruebas.

example:  
```python
    @pytest.fixture  
    def username():  
        yield '<username>'  
```

nota: La utilizacion de yield en las pruebas unitarias mediantes  
      metodos de funciones, es para simular la [setup] y [teardown]  
      que tiene las clases y los metodos de las clases.  


### Parametrizaci??n de pruebas 

Las parametrizacion de las pruebas unitarias, nos dan la facilidad de automatizar  
y realizar [n] cantidad de veces una prueba. 

Para poder parametrizar una prueba lo primero que tenemos que hacer es darle  
nombres a los argumentos que necesitamos para llevar a cabo el test:

example:

```python
        def test_new_task(self, title, descripcion, assigned_to, due_date):  
                task = Task(title, descripcion, assigned_to. due_date)  

                assert task.title == title  
                assert task.description == descripcion  
                assert task.assigned_to == assigned_to  
                assert task.due_date == due_date   
```

despues de eso pasamos al segundo paso, en que decoramos la funcion de prueba  
de la siguiente forma en el paso (2) en donde la mark.parametrize() recibe 2  
argumentos los cuales son un string y una lista de tuplas:  
[string] => en esta tiene que ir los nombre de los argumentos que pasaremos  
            a la funcion de prueba. y   

[list] =>   en esta tiene iran un listado de tuplas con el orden de los  
            parametros que pasaremos, segun la cantidad de tuplas incluidad  
            aqui, asi seran las cantidad de veces que se repetira la prueba.  
```python
#(2)     
        @pytest.mark.parametrize(  
                'title, description, assigned_to, due_date',
                [
                        ('title 1', 'description 1', 'assigned_to', 'due_date')
                ]

        )
#(1)     
        def test_new_task(self, title, descripcion, assigned_to, due_date):  
                task = Task(title, descripcion, assigned_to. due_date)  

                assert task.title == title  
                assert task.description == descripcion  
                assert task.assigned_to == assigned_to  
                assert task.due_date == due_date   
```

### Cobertura de C??digo
Es una medida de porcentual, el cual no dice que pocentaje de nuestro codigo a sido  
ejecutado y tambien probado.  

y para poder ver oportunidades de mejora en nuestro codigo, y poder refactorizar.

utilizaremos la libreria [coverage] en un entorno virtual

```bash
        python -m pip install coverage
```

example:

```bash
        coverage run -m pytest app/test/test_task.py
#salidad
        ============================= test session starts ==============================
        platform linux -- Python 3.10.4, pytest-7.2.0, pluggy-1.0.0
        rootdir: /workspaces/unittes/Test_Pytest/app/test, configfile: pytest.ini
        collected 10 items

        app/test/test_task.py ........s.                                         [100%]

        ========================= 9 passed, 1 skipped in 0.02s =========================
```

Despues de aver ejecutado el [ coverage run ] en nuestros documentos se genera un documento  
con [ .coverage ] en donde esta resumidor los resultados de la ejecucion de nuestro codigo.  

para ver este resumen o reporte solo tenemos que ejecutar lo siguientes en la consola.  

```bash
        coverage report
#salida

        Name                    Stmts   Miss  Cover
        -------------------------------------------
        app/__init__.py             0      0   100%
        app/task.py                11      0   100%
        app/test/__init__.py        0      0   100%
        app/test/test_task.py      44      1    98%
        -------------------------------------------
        TOTAL                      55      1    98%
```

como se puede ver en el reporte solo del script test_task.py tenemos [ Miss 1 ]  
eso quiere decir que no se ejecuto a su 100%. y para ver que linea fue la que no  
se ejecuto solo tenemos que pasas el flag -m de la siguiente forma.

```bash
        coverage report -m
#salida

        Name                    Stmts   Miss  Cover   Missing
        -----------------------------------------------------
        app/__init__.py             0      0   100%
        app/task.py                11      0   100%
        app/test/__init__.py        0      0   100%
        app/test/test_task.py      44      1    98%   64
        -----------------------------------------------------
        TOTAL                      55      1    98%
``` 

en la columna [ Missing ] no da un resultado para el script test_task.py de 64 en cual  
corresponde al numero de la linea que no se a ejecutado.
