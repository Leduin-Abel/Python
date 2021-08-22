#import test22_modulos
#Python busca los modulos en el mismo directorio de donde lo llamen
#facilita las cosas, me permite quitar el nombre del modulo
from test22_modulos import * #El asterisco me permite importar todo
sumar(3,4)
multiplicar(6,9)
restar(9,10)

#para utilizar paquetes(modulos que no están en la misma carpeta que se les llama)
from paq.cal import redondear #carpeta.archivo

redondear(6.987)


#para utilizar subpaquetes
from paq.basicas.sum import * #seguir la ruta del archivo paquete princ.subpaq.archivo

sumar(1,2)

from paq.redondeo_pot.red_pot import *

potencia(3,901)