#superclase
class vehiculos():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True
    
    def estado(self):
        print("Marca; ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",self.enmarcha, 
        "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


class furgoneta(vehiculos):
    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"
#Herencia 
class Moto(vehiculos): #Dentro de parentesis va de donde se hereda
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo caballito"

    #sobre escribiendo estado, el programa solo toma el sobreescrito e ignora el original
    def estado(self):
        print("Marca; ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",self.enmarcha, 
    "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)

class VELectricos(vehiculos):
    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)
        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True
miMoto=Moto("honda", "CBR")

miMoto.caballito()

miMoto.estado() 

miFurgoneta=furgoneta("P", "LEL")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))

#Cuando hay herencia multiple se le da preferencia a la primera clase
class BicicletaElectrica(VELectricos, vehiculos):
    def estado(self):
        print("Marca; ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",self.enmarcha, 
        "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


miBici=BicicletaElectrica("AAA", "ADAAd")

miBici.estado()
