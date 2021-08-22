import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

#borrado de datos
miCursor.execute("DELETE FROM PRODUCTOS3 WHERE ID= 1")

#actualización de datos
#miCursor.execute("UPDATE PRODUCTOS3 SET PRECIO=35 WHERE NOMBRE_ARTICULO='PELOTA'")

#lectura de datos
"""miCursor.execute("SELECT * FROM PRODUCTOS3 WHERE SECCION='CONFECCIÓN'")


productos=miCursor.fetchall()

print(productos)"""


miConexion.commit()

miConexion.close()