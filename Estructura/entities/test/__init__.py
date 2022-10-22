"""
    Se crea una carpeta, y dentro de la carpeta.
    Para que la carpeta sea tratada como un modulo en python,
    y esta sera para los test que se realizaran en el proyecto
    y para realizar estar pruebas,
    se ejecutarn de la siguientes forma:

    Example:
        #Todo el modulo
    1 - python -m unittest [diretorio.prueba.modulo] 
        #Solo esa Clase
    2 - python -m unittest [diretorio.prueba.modulo.clases] 
        #Solo ese metodo
    3 - python -m unittest [diretorio.prueba.modulo.clases.metodos] 
        #Esto ejecutara todas las pruebas de todas las clases y modulos.
    4 - python -m unittest -v discover 
"""