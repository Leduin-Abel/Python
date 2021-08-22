class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        
        self.cargo=cargo

        self.salario=salario
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[
    Empleado("Juan", "Director", 5000),
    Empleado("Ana", "CEO", 9000),
    Empleado("TU", "Admin", 4000),
    Empleado("L", "Dueño", 10000)
]

def calculo_comision(empleado):
    empleado.salario=empleado.salario*1.03
    return empleado

listaEmpleadosComision=map(calculo_comision,listaEmpleados) #en vez de filtrar le aplica una función a una lista de elementos

for empleado in listaEmpleadosComision:
    print(empleado)