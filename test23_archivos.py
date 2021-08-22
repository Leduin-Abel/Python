from io import open

#puedo abrir archivos en modo lectura, escritura o append(para agregar info)
text=open("archivo.txt","w") #si no existe el archivo, lo crea//w es para modo escritura
frase="Hola como estás?\nAAAAAAAAAAAAAAAAA"

#para incluir en el archivo
text.write(frase)#pide lo que quiero añadir

#para cerrar
text.close

text=open("archivo.txt","r")# r es modo lectura
lect=text.read()
text.close()
print(lect)

text=open("archivo.txt","r")

#lee las lineas de texto
lineas=text.readlines()
text.close()
print(lineas)

text=open("archivo.txt", "a")#a es modo append, para agregar
text.write("\nbien y tu?")
text.close()
text=open("archivo.txt","r") #r+ lectura y escritura
print(text.read(11))#una vez termina la lectura, el cursero queda en la posición indicada
#permite controlar la posición del cursor, le entra la posición del caracter donde quiero ponerlo
#text.seek(0)

print(text.read()) #lee hasta el caracter que le indique
