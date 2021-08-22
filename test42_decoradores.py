def funcion_decoradora(funcion_parametro):
    #def funcion_interior():#sin parametros
    #def funcion_interior(*args): #*args recibe un numero indeterminado de parametros
    def funcion_interior(*args, **kwargs):#**kwargs son keywords arguments
        #Acciones adicionales que decoran
        print("Vamos a realizar un cálculo: ")

         #funcion_parametro() #sin parametros 
        #funcion_parametro(*args)#Aquí también debe estar
        funcion_parametro(*args, **kwargs)#Aquí también va lo de keywords arguments
        #Acciones adicionales que decoran

        print("Hemos terminado el cálculo")

    return funcion_interior


@funcion_decoradora #decoracion
def suma(num1,num2,num3):
    print(num1+num2+num3)

@funcion_decoradora
def resta(num1,num2):
    print(num1-num2)
    
@funcion_decoradora
def potencia(base,exponente):
    print(pow(base,exponente))


suma(7,5,67)

resta(12,10)

potencia(base=5,exponente=3)#base y exponente son las claves de la funcion, 5 y 3 son valores, para esto debemos ingresar el kwargs (clave:valor)