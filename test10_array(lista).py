A=["pu","qo","io","t"]

#toda la lista
print(A[:])

#Del indice uno en adelante
print(A[1:])

#Del indice uno hasta el 2
print(A[1:3])

#Hasta el tres
print(A[:3])

#Inserta elementos al final
A.append("h")
print(A[:])

#Inserta elementos donde quiera, pide indice y elemento
A.insert(2,"y")
print(A[:])

#Agregar varios datos(como si concantenara listas)
A.extend(["h","y","o"])
print(A[:])

#Devuelve el indice
print(A.index("h"))


#Dice si está o no un elemento
print("y" in A)

#Elimina un elemento
A.remove("h")

print(A[:])

#Elimina el ultimo elemento de la lista
A.pop()
print(A[:])

#+ sirve como .extend
A=["N", 2, False, 78.91] 
B=["Q","e"]
C=A+B

print(C[:])


#* es un repetidor
D=["A",4, False, 90.123]*3
print(D[:])
A=A*3
print(A[:])




