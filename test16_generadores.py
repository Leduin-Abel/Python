def generapares(limite):
    num=1
    lista=[]
    while num<limite:
        lista.append(num*2)
        num=num+1
    return lista

print(generapares(5))

#Ahora con un generador
def generapares2(limite2):
    num2=1
    while num2<limite2:
        yield num2*2

        num2+=1
devuelvepares=generapares2(5)


#con el método next, cada next me permite acceder a un valor unico del generador
print(next(devuelvepares))

print("AAAA")

print(next(devuelvepares))

print("AAAA")

print(next(devuelvepares))
print(next(devuelvepares))

#El astericos significa que recibiriá una cantidad indeterminada de elementos y los recibirá como una tupla
# def devuelve_ciudades(*ciudades):
#     for elem in ciudades:
#         for subelem in elem:
#             yield subelem
# ciud=devuelve_ciudades("Madrid", "Barcelona","Bilbao", "Valencia")

# print(next(ciud))

# print(next(ciud))


#yield from
def devuelve_ciudades(*ciudades):
    for elem in ciudades:
        #for subelem in elem:
        yield from elem
        
            

ciud2=devuelve_ciudades("Madrid", "Barcelona","Bilbao", "Valencia")

print(next(ciud2))

print(next(ciud2))
