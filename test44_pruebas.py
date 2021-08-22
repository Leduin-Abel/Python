def areaTriangulo(base,altura):
    """
    Calcula el área de un triangulo

    >>> areaTriangulo(3,6)
    8.0

    """
    #la prueba va con >>> y justo debajo va lo que exactamente debería devolver, va dentro de las comillas triples
    return(base*altura)/2

import doctest

doctest.testmod()#gracias a esto realiza la prueba, no muestra nada si NO hay problemas