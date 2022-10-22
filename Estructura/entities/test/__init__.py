"""
    Se crea una carpeta, y dentro de la carpeta.
    Para que la carpeta sea tratada como un modulo en python,
    y esta sera para los test que se realizaran en el proyecto
    y para realizar estar pruebas,
    se ejecutarn de la siguientes forma:

    Example:
    1 - python -m unittest [diretorio.prueba.modulo] #todo el modulo
    2 - python -m unittest [diretorio.prueba.modulo.clases] #solo esa Clase
    3 - python -m unittest [diretorio.prueba.modulo.clases.metodos] #solo ese metodo
    4 - python -m unittest -v discover #esto ejecutara todas las pruebas de todas las clases y modulos.
"""