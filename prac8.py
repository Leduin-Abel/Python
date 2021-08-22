print("Ingrese su contraseña, recuerde que debe tener mas de 8 caracteres y no puede tener espacios en blanco")
contr=input("Ingrese su contraseña: ")

t=0
cont=0
for i in contr:
    cont=cont+1
    if i==" ":
        print("Contraseña erronea")
        t=1

if cont<8 and t==0:
    print("Contraseña erronea")
elif cont>=8 and t==0:
    print("Contraseña OK")

