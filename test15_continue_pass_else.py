for letra in "Python":
    if letra=="h":
        #se salta el resto del bucle y va a la siguiente iteración
        continue
    print(letra)


#pass ignora lo que sigue

email=input("meta su email mi fai: ")
for i in email:
    if i=="@":
        arroba=True
        break;
#diferente del else del if, entra una vez que el for termine  , tambien sirve en el while     
else:
    arroba=False
print(arroba)