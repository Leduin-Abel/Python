import pickle
#creación archivo bin
nombres=["Pedro", "Ana", "Juan", "Andres"]

arch_bin=open("lista_nombres", "wb")#wb es escritura binaria

pickle.dump(nombres,arch_bin)#recibe la información a echar y el archivo

arch_bin.close()

del(arch_bin)

#rescate archivo binario
text=open("lista_nombres","rb")#rb es lectura binaria

lista=pickle.load(text)#carga el archivo

print(lista)
