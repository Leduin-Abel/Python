class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camión():
    def desplazamiento(self):
        print("Me desplazo utilizando seis reudas")

#poliformismo
def desplazamientovehiculo(vehiculo):
    vehiculo.desplazamiento()

mivehiculo=Coche()

desplazamientovehiculo(mivehiculo)