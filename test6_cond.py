nom=input("Ingresa tu nombre: ")
num1=float(input("nota1: "))
num2=float(input("nota2: "))
num3=float(input("nota3: "))

prom=(num1+num2+num3)/3

if prom>=3:
    print('Crack '+ nom +  ' pasaste con promedio de: ', prom)
    print('Crack '+ nom +  ' pasaste con promedio de: ', round(prom,4))
else:
    print('Yaper' + nom +' figuró repetirla')
    print('Te quedó en: ', round(prom,4))


print("Fin")

y=False

#Pregunta si la variable es true de manera implicita
if y:
    print("tuki")
else:
    print("no tuki")

