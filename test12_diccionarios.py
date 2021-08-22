#Almacena datos de manera valor:clave
dicc={"Alemania":"Berlín","Francia":"París","Reino Unido":"Londres","Colombia":"Quibdó"}

#Siempre regresa el valor ante una clave
print(dicc)

#Agrega más parejas
dicc["Italia"]="PUTAS"

print(dicc)

#Para modificarlo (se sobrescribe)
dicc["Italia"]="Roma"
print(dicc)

#Para eliminar elementos
del dicc["Reino Unido"]
print(dicc)

#cosas variadas
dicc2={"A":"B", 23:"Jordan", "Zorras":4}
print(dicc2)

#tupla en dicc(también es posible con listas)
tup=("España", "Francia", "Reino Unido", "Alemania")
dicc3={tup[0]:"madrid", tup[1]:"paris", tup[2]:"londres", tup[3]:"berlin"}
print(dicc3)

#Mas cosas
dicc4={23:"Jordan", "nombre":"michael", "equipo":"chicago", "anillos":[1,2,3,4,5,6]}
print(dicc4["anillos"])

#diccionario dentro de diccionario
dicc5={23:"Jordan", "nombre":"michael", "equipo":"chicago", "anillos":{"temporadas":[1,2,3,4,5,6]}}
print(dicc5)

#devuelve las claves
print(dicc5.keys())

#devuelve los valores
print(dicc5.values())

#devuelve la longitud
print(len(dicc5))





