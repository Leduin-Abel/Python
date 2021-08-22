import pickle 

class Persona:
    def __init__(self,nombre,genero,edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre de: ", self.nombre)

    def __str__(self):#convierte en cadena la informacion
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class Listapersonas:
    personas=[]

    def __init__(self):
        listadepersonas=open("externo", "ab+")#agregar información binaria
        listadepersonas.seek(0)
        try:
            self.personas=pickle.load(listadepersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except: 
            print("El fichero está vacío")
        finally:
            listadepersonas.close()
            del(listadepersonas)


    def agregarPersonas(self,p):
        self.personas.append(p)
        self.guardarPersonasEnExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnExterno(self):
        listapersonas=open("externo","wb")
        pickle.dump(self.personas,listapersonas)
        listapersonas.close()
        del(listapersonas)

    def mostrarInfoExterno(self):
        print("La información del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)


miLista=Listapersonas()
persona=Persona("o", "u", 3)
miLista.agregarPersonas(persona)
miLista.mostrarInfoExterno()
#p=persona("Antonio", "Masculino", 89)
#miLista.agregarPersonas(p)
#p=persona("Laura", "Femenino", 29)
#miLista.agregarPersonas(p)

#miLista.mostrarPersonas()