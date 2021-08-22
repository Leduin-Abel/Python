print("================================================================================")
print("Bienvenido, por favor ingrese sus datos y sabrá sus dias de vacaciones asignados")
print("===============================================================================\n")

nom=input("Ingrese su nombre: ")
ser=int(input("Ingrese sus años de servicio: "))
print("\nSeleccione su caso:\n")
print("Seleccione 1 si es de atención al cliente")
print("Seleccione 2 si es de logística")
print("Seleccione 3 si es de gerencia")
opc=int(input("Ingrese su selección: "))

if opc == 1:
    if ser ==1:
        print( nom + ', usted tiene derecho a 6 días de vacaciones\n')
    elif ser >1 and ser <=6:
        print( nom + ', usted tiene derecho a 14 días de vacaciones\n')
    elif ser>=7:
        print( nom + ', usted tiene derecho a 20 días de vacaciones\n')
    else:
        print("Por favor seleccione una opción válida")
elif opc==2:
    if ser==1:
        print( nom + ', usted tiene derecho a 7 días de vacaciones\n')
    elif ser>1 and ser <=6:
        print( nom + ', usted tiene derecho a 15 días de vacaciones\n')
    elif ser >=7:
        print( nom + ', usted tiene derecho a 22 dias de vacaciones\n')
    else:
        print("Por favor seleccione una opción válida")
elif opc==3:
    if ser ==1:
         print( nom + ', usted tiene derecho a 10 días de vacaciones\n')
    elif ser>1 and ser <=6:
        print( nom + ', usted tiene derecho a 20 días de vacaciones\n')
    elif ser >=7:
        print( nom + ', usted tiene derecho a 30 dias de vacaciones\n')
    else:
        print("Por favor seleccione una opción válida")
else:
    print("Por favor ingrese una opción válida")
    
