import math

def raizCuadrada(listaNumeros):
   
    """
    La función devuelve una lista con la 
    raíz cuadrada de los elementos númericos 
    pasados por parámetros en otra lista


    >>> lista=[]
    >>> for i in [4,9,16]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    [2.0, 3.0, 4.0]

    >>> lista=[]
    >>> for i in [4, -9, 16]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    Traceback (most recent call last):
     ...
    ValueError: math domain error
 



    """
    #para expresiones anidadas se utilizan 3 puntos
    #tambien se utilizan para excepciones
    return[math.sqrt(n) for n in listaNumeros]

#print(raizCuadrada([9, -16, 25, 36]))

import doctest

doctest.testmod()