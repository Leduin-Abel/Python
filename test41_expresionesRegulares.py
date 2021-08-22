import re

cadena="Vamos a aprender expresiones regulares"

textobuscar="aprender"

if re.search(textobuscar,cadena) is not None: #search busca algo en una cadena texto y devuelve un objeto si lo encuentra y none si no
    print("He encontrado el texto")
else:
    print("No he encontrado el texto")

textoEncontrado=re.search(textobuscar,cadena)

print(textoEncontrado.start())#caracter inicial donde esta lo encontrado

print(textoEncontrado.end())#caracter final de lo encontrado

print(textoEncontrado.span())#devuelve una tupla donde inicia y donde termina

cadena="Vamos a aprender exxpresiones regulares en Python. Python es un lenguaje sencillo"

textobuscar="Python"

print(len(re.findall(textobuscar,cadena)))#devuelve  todas las veces que este lo que se busca

#metacaracteres
#anclas
lista_nombres=['Ana Gomez', 'Maria Martín','Sandra López','Santiago Martín', 'Sandra Fernandez']

for elemento in lista_nombres:
    if re.findall('^Sandra', elemento): #^ es el metacaracter, es el ancla, busca en la lista elementos que comiencen por  en este caso sandra
        print(elemento)

for elemento in lista_nombres:
    if re.findall('Martín$', elemento): # $ es el metacaracter, me devuelve los que terminen por en este caso Martin
        print(elemento)