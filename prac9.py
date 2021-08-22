cor=input("Ingrese su correo: ")
cont=0

for i in range(len(cor)):
    if cor[i]=="@" or cor[i]==".":
        cont=cont+1
if cont>=2:
    print("Correo correcto")
else:
    print("Revise")



