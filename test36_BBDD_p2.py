import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()
#modo manual de asignar el campo clave
"""miCursor.execute(''' CREATE TABLE PRODUCTOS(
        CODIGO_ARTICULO VARCHAR (4) PRIMARY KEY, 
        NOMBRE_ARTICULO VARCHAR(50), 
        PRECIO INTEGER,
        SECCION VARCHAR(20))
        ''')"""

"""productos=[
    ("AR01", "PELOTA", 20, "JUGETERÍA"),
    ("AR02", "PANTALÓN",15 , "CONFECCIÓN"),
    ("AR03", "DESTORNILLADOR",25, "FERRETERÍA"),
    ("AR04","JARRÓN", 45, "CERÁMICA")
]"""


#modo automatico
miCursor.execute(''' CREATE TABLE PRODUCTOS3(
        ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        NOMBRE_ARTICULO VARCHAR(50), 
        PRECIO INTEGER,
        SECCION VARCHAR(20))
        ''')
productos=[
    ("PELOTA", 20, "JUGETERÍA"),
    ("PANTALÓN",15 , "CONFECCIÓN"),
    ("DESTORNILLADOR",25, "FERRETERÍA"),
    ("JARRÓN", 45, "CERÁMICA")

]


miCursor.executemany("INSERT INTO PRODUCTOS3 VALUES (NULL, ?, ?, ?)",productos)#null porque se autoincrementa, si no fuese así toca poner el otro interrogante


miConexion.commit()

miConexion.close()