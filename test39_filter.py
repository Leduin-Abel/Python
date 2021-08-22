'''def num_par(num):
    if num % 2==0:
        return True'''
#filter devuelve objetos a los cuales una función(Creada por el usuario) devuelve true
'''numeros=[17,24,5,39,8,51,92]

print(list(filter(lambda numero_par:numero_par%2==0,numeros)))'''

class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        
        self.cargo=cargo

        self.salario=salario
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[
    Empleado("Juan", "Director", 75000),
    Empleado("Ana", "CEO", 95000),
    Empleado("TU", "Admin", 30000),
    Empleado("L", "Dueño", 99999999)
]

salarios_altos=filter(lambda empleado: empleado.salario>50000,listaEmpleados)

for empleado_salario in salarios_altos:
    print(empleado_salario)
