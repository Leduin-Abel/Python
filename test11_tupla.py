#Tupla=lista no modificable, pero permite el index
#Van con parentesis 
tup=("P",2,13,99)

#Permite hacer que una tupla se vuelva lista
A=list(tup)

#Las listas se imprimen con parentesis, las listas con corchete
print(A)
print(tup)

#Permita hacer una lista en una tupla
B=("P",8,5,109,5)
tup2=tuple(B)

print(B)
print(tup2)

#Permite saber si un elemento está dentro de una tupla
print("P" in tup)

#Permite saber cuantas veces está un elemento dentro de una tupla
print(tup2.count(5))

#Permite saber la cantidad de elementos que tiene la tupla
print(len(tup2))

#para crear una tupla unitaria la sintaxis debe ser:
tup3=("o",)
print(len(tup3))

#Se puede asignar los elementos de la tupla a cada variable por  orden
r,y,u,s,d=tup2
print(tup2)
print(r)
print(u)
print(d)
print(y)
print(s)
