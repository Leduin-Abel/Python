def div1(num1,num2):
    #Captura de erroes
    #Intenta ejecutar la instrucción, si no se puede ejecuta el except
    try:
        return num1/num2
    #solo entra si es ese error y si no es, se detiene el programa
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operación errónea"


#op1=float(input("num1: "))
#op2=float(input("num2: "))


#print(div1(op1,op2))


def div2():
    try:
        op3=float(input("num1: "))
        op4=float(input("num2: "))
        print("La división es: " + str(op3/op4))
    except ValueError:
        print("Numeros corretos porfi")
    except ZeroDivisionError:
        print("No se puede")
    #ejecuta siempre lo que vaya dentro haya o no error
    finally:
        print("Fin")

#div2()

def div3():
    try:
        op3=float(input("num1: "))
        op4=float(input("num2: "))
        print("La división es: " + str(op3/op4))
    #No importa el error entra al except
    except:
        print("Hay un error")
    print("Fin")
#div3()


def evEdad(edad):
    if edad<0:
        #permite crear mis propias excepciones, del tipo que yo desee con el mensaje que yo quiera
        raise TypeError("No se permiten edades negativas")
    if edad <20:
        return "Eres muy joven"
    elif edad<40:
        return"Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuidate"
print(evEdad(90))

import math
def raiz(num1):
    if num1<0:
        raise ValueError ("El número no puede ser negativo")
    else:
        return math.sqrt(num1)

op1=(int(input("Introduce número: ")))

try:
    print(raiz(op1))
#Me permite llamar un raise anterior con sus instrucciones
except ValueError as ErrorNumNeg:
    print(ErrorNumNeg)
print("Fin")
