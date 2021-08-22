import pickle

class vehiculo():
    def __init__(self, marca, modelo):
        
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
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha,
        "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

coche1=vehiculo("Mazda", "MX5")    

coche2=vehiculo("Lambo", "urus")    

coche3=vehiculo("Chevrolet", "ranger")    

coches=[coche1,coche2, coche3]

text=open("Loscoches", "wb")

pickle.dump(coches,text)

text.close()

del(text)

arch=open("Loscoches","rb")

misCoches=pickle.load(arch)

arch.close()

for c in misCoches:
    print(c.estado())