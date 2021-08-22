for i in ["primavera","verano","otoño","invierno"]:
    #comando end sirve para ignorar el salto de linea
    print("hola", end=" ")

#recorre caracter a caracter
for i in "leduin@siempresuen":
    #imprime el mensajes tantas veces como caracteres haya
    print("Jola", end="")

#Funciona como un for clasico
#Range genera tantos numeros como se le pidan iniciando desde 0 
for i in range(9):
    print(i)

#Permite hacer conteos en un rango que va desde el númmero inicial hasta uno antes que el final, y permite de cuanto en cuanto
for i in range(5,50,5):
    #notación permite combinar texto y variable
    print(f"valor de la variable {i}")



