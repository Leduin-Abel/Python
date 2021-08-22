corr=input("Ingrese su correo crack: ")

cont=corr.count("@")
posa=corr.find("@")
posb=corr.rfind("@")
larg=len(corr)
t=larg-1
print(t)
print(cont)
print(posa)
print(posb)
if(cont==1 and posa!=0 and posb!=t):
    print("La dirección es correcta")     
else:
    print ("Yaper")