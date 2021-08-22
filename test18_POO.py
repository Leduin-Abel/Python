#Creación de clase
class Coche():
    #Método constructor, les da estado inicial a los objetos
    def __init__(self): #sin esto solo serían las propiedades e irian sin el self.
        #propiedades de clase
        self._largochasis=250
        self._anchochasis=120
        #encapsulamiento de ruedas, nada fuera de la clase puede acceder ella(siempre que la llame debe ir con UN guin bajos)
        self._ruedas=4 #UN guión bajo para encapsular
        self._enmarcha=False

    #comportamiento, lo determinan los métodos
    #Def de método, método es una función especial que pertenece a una clase 
    def arranchar(self,arrancamos): #self referencia al objeto perteneciente a la clase
    #def arranchar(self)     
        self._enmarcha=arrancamos
        if(self._enmarcha):
            chequeo=self._chequeo()
        if(self._enmarcha and chequeo):
            return "El coche está en marcha"

        elif(self._enmarcha and chequeo==False):
            return "Algo ha ido mal, no se puede arrancar"

        else:
            return "El cohce está parado"
        

    def estado(self):
        print("El coche tiene ", self._ruedas, "ruedas. Un ancho de ", self._anchochasis, " y un largo de ",
        self._largochasis)
    
    def _chequeo(self): #encapsulado de metodo (UN guión bajo), solo puedo acceder a él dentro de la clase
        print("Voa realizar un chequeo")
        self.gasolina="ok"
        self.aceite="ok"
        self.puerta="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puerta=="cerradas"):
            return True
        else:
            return False
        
    
#objeto; instanciar//ejemplarizar la clase 
micoche=Coche()

#nomenclatura del punto
print(micoche._largochasis)
print(micoche._ruedas)
#micoche.arranchar() #Recibe como parametro el propio objeto(obra de self)
print(micoche.arranchar(True))#Debe recibir un parametro ya que le agregué algo más del self
micoche.estado()

print("--------------Nuevo objeto--------------")

micoche2=Coche()
print(micoche2._largochasis)
print(micoche2._ruedas)
print(micoche2.arranchar(False))

#modificando el valor de la propiedad(no funciona porque está encapsulada)
micoche2.ruedas=2
micoche2.estado()

