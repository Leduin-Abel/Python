import sqlite3

miConexion=sqlite3.connect("PrimeraBase")#crea base de datos
miCursor=miConexion.cursor()#puntero
#creacion lista
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR (50), PRECIO INTEGER, SECCION VARCHAR(20))")#lenguaje SQL dentro del parentesis, nombre lista y tipo

#ingreso de datos
miCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALÓN',15,'DEPORTES')")

miConexion.commit()


miConexion.close()