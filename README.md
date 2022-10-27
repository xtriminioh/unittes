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



