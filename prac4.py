def max(num1,num2):
    if num1>num2:
        return(num1)
    elif num2>num1:
        return(num2)
    else:
        return(1)

t=float(input("Ingrese un número: "))
u=float(input("Ingrese otro número: "))

r=max(t,u)
if r!=1:
    print("\n El número más grande es", r)
else:
    print("Los numeros son iguales")
    
print("\n Fin")
