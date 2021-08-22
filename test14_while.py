import math
ed=int(input("Dime tu edad: "))
while ed<=0:
    print("Deja la maricada!")
    ed=int(input("Dime tu edad: "))


print("La buena") 
print("Tu edad es " + str(ed))

print("Que se dice?")
num=float(input("Introduce un nuúmero: "))

intentos=0
while num<0:
    print("No se puede hallar la raíz de un número negativo")

    if intentos==2:
        print("yamile perdomo")
        #permite terminar el while
        break;
    num=float(input("mete un numero bueno"))
    if num<0:
        intentos=intentos+1
if intentos<2:
    #math. es una clase 
    sol=math.sqrt(num)
    print("La raíz cuadrada de " + str(num) + " es " + str(sol))
