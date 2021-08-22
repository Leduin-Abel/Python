class persona():
    def __init__(self,nombre,edad, lugar_residencia):
        
        self.nombre=nombre

        self.edad=edad

        self.lugar_residencia=lugar_residencia
    
    def descripcion(self):
        print("Nombre: ", self.nombre, " Edad: ", self.edad, " Residencia: ", self.lugar_residencia)

class Empleado(persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        #Me permite llamar un metodo de la clase padre, (en este caso el init)    
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        
        self.salario=salario
        
        self.antiguedad=antiguedad
    def descripcion(self):
        super().descripcion()
        
        print("Salario: ", self.salario,"Antiguedad: ",  self.antiguedad)


manolo=persona("Manolo", 52, "Colombia")
manolo.descripcion()

#Permite saber si un objeto pertenece a una clase,
print(isinstance(manolo, Empleado))
