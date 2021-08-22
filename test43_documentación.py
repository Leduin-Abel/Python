import test22_modulos
class Areas:
    """Informacion"""
    def areaCuadrado(Lado):
        """Calcula el área de un cuadrado elevando al cuadrado el lado pasado por parámetro"""
    
        return "El área del cuadrado es: " + str(Lado*Lado)

    def areaTriangulo(base,altura):
        """ Mas información"""
    
        return "El área del triángulo es: " + str((base*altura)/2)

#print(areaCuadrado(5))

#cuando son funciones independientes
#print(areaCuadrado.__doc__)#devuelve la documentación(comentarios con triple comilla) de la función
#help (areaCuadrado)#imprime info sobre la función

#cuando hacen parte de una clase 
#help(Areas.areaCuadrado)
#help(Areas)#ayuda general de la clase
help(test22_modulos)