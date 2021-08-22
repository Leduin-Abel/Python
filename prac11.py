from tkinter import * 
from tkinter import messagebox
import sqlite3


raiz=Tk()
def salirAplicacion():
    #valor=messagebox.askquestion("Salir", "¿Se quiere ir maquina?")#devuelve yes or no
    valor=messagebox.askokcancel("Salir", "¿Se quiere ir maquina?")#devuelve true or false
    if valor==True:
        raiz.destroy()

def infoAddicional():
    messagebox.showinfo("AAAAAAAAAAAAAA","BBBBBBBBBBBB")

def avisoLicencia():
    messagebox.showwarning("ASDASDas","AAAA")

def borraCampos(idd,nom,pasw,ap,dirr,com):
    valor=messagebox.askokcancel("Borrar", "¿Seguro que desea borrar la información?")
    if valor:
        idd.delete(0,'end')
        nom.delete(0,'end')
        pasw.delete(0,'end')
        ap.delete(0,'end')
        dirr.delete(0,'end')
        com.delete(1.0,'end')

def creaBase():
    try:
        miConexion=sqlite3.connect("Base")
        miCursor=miConexion.cursor()
        miCursor.execute(''' CREATE TABLE INFORMACION(
        ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        NOMBRE_USUARIO VARCHAR(20), 
        CONTRASEÑA VARCHAR(20),
        APELLIDO VARCHAR(20),
        DIRECCION VARCHAR (20),
        COMENTARIOS VARCHAR(100))
        ''')
    except sqlite3.OperationalError or OperationalError:
        messagebox.showerror("Error", "La base ya existe")

    miConexion.commit()
    miConexion.close()

def actualizaBase(nom,pasw,ap,dirr,com):
    miConexion=sqlite3.connect("Base")
    miCursor=miConexion.cursor()
    nombre=nom.get()
    password=pasw.get()
    appellido=ap.get()
    direccion=dirr.get()
    comentario=com.get(1.0,'end')
    if (nombre=="" and password=="" and appellido=="" and direccion=="" and comentario==""):
        messagebox.showerror("Error", "No hay información que añadir") 
    else:
        info=(nombre,password,appellido,direccion,comentario)
        try:
            miCursor.execute('INSERT INTO INFORMACION VALUES (NULL, ?, ?,?,?,?)',info)
        except sqlite3.OperationalError:
    
            messagebox.showerror("Error","La base no existe")
    miConexion.commit()
    miConexion.close()

def leeBase():
    miConexion=sqlite3.connect("Base")
    miCursor=miConexion.cursor()
    
    miCursor.execute("SELECT * FROM INFORMACION WHERE ID=" + miID.get())
    datos=miCursor.fetchall()
    for user in datos:
        miID.set(user[0])
        minombre.set(user[1])
        miPass.set(user[2])
        miApellido.set(user[3])
        miDireccion.set(user[4])
        textoComentario.insert(1.0,user[5])
    miConexion.commit()
def borrar():
    miConexion=sqlite3.connect("Base")
    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM INFORMACION WHERE ID=" + miID.get())
    miConexion.commit()

miFrame=Frame(raiz,width=1200, height=200)
miFrame.pack()

raiz.title("PRACTICA 11")

#cuadros de texto

miID=StringVar()
cuadroID=Entry(miFrame, textvariable=miID)#probablemente genere problemas
cuadroID.grid(row=0,column=1, padx=5, pady=5,columnspan=4)

minombre=StringVar()
cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=1,column=1,padx=5,pady=5,columnspan=4)

miPass=StringVar()
cuadroPass=Entry(miFrame,textvariable=miPass)
cuadroPass.grid(row=2,column=1,padx=5,pady=5,columnspan=4)
cuadroPass.config(show="¬")

miApellido=StringVar()
cuadroApellido=Entry(miFrame,textvariable=miApellido)
cuadroApellido.grid(row=3,column=1,padx=5,pady=5,columnspan=4)

miDireccion=StringVar()
cuadroDirección=Entry(miFrame,textvariable=miDireccion)
cuadroDirección.grid(row=4,column=1,padx=5,pady=5,columnspan=4)

textoComentario=Text(miFrame,width=16,height=5)
textoComentario.grid(row=5,column=1,padx=5,pady=5,columnspan=4)
barravert=Scrollbar(miFrame,command=textoComentario.yview)
barravert.grid(row=5,column=4,sticky="nsew")
textoComentario.config(yscrollcommand=barravert.set)

#LABEL
nombreLabel=Label(miFrame,text="ID:")
nombreLabel.grid(row=0,column=0, sticky="e",padx=5,pady=5)

nombreLabel=Label(miFrame,text="Nombre:")
nombreLabel.grid(row=1,column=0, sticky="e",padx=5,pady=5)

passLabel=Label(miFrame,text="Contraseña:")
passLabel.grid(row=2,column=0,sticky="e",padx=5,pady=5)

apellidoLabel=Label(miFrame,text="Apellido: ")
apellidoLabel.grid(row=3,column=0,sticky="e",padx=5,pady=5)

direccionLabel=Label(miFrame,text="Dirección:")
direccionLabel.grid(row=4,column=0,sticky="e",padx=5,pady=5)

comentariosLabel=Label(miFrame,text="Comentarios:")
comentariosLabel.grid(row=5,column=0,sticky="e",padx=5,pady=5)

#Menus
barraMenu=Menu(raiz)
raiz.config(menu=barraMenu,width=300, height=300)

archivoBBDD=Menu(barraMenu,tearoff=0) 
barraMenu.add_cascade(label="BBDD", menu=archivoBBDD) 
archivoBBDD.add_command(label="Conectar")
archivoBBDD.add_command(label="Salir", command=salirAplicacion)

archivoBORRAR=Menu(barraMenu,tearoff=0) 
barraMenu.add_cascade(label="BORRAR", menu=archivoBORRAR) 
archivoBORRAR.add_command(label="Borrar campos",command=lambda:borraCampos(cuadroID,cuadroNombre,cuadroPass, cuadroApellido,cuadroDirección,textoComentario))


archivoCRUD=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="C.R.U.D", menu=archivoCRUD) 
archivoCRUD.add_command(label="CREATE",command=creaBase)
archivoCRUD.add_command(label="READ", command=leeBase)
archivoCRUD.add_command(label="UPDATE",command=lambda:actualizaBase(cuadroNombre,cuadroPass, cuadroApellido,cuadroDirección,textoComentario))
archivoCRUD.add_command(label="DELETE",command=borrar)


archivoAyuda=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda) 
archivoAyuda.add_command(label="Licencia",command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAddicional)


#Botones
botonCREATE=Button(miFrame, text="CREATE", command=creaBase)
botonCREATE.grid(row=6,column=0,padx=5,pady=5)

botonREAD=Button(miFrame, text="READ",command=leeBase)
botonREAD.grid(row=6,column=1,padx=5,pady=5)

botonUPDATE=Button(miFrame, text="UPDATE",command=lambda:actualizaBase(cuadroNombre,cuadroPass, cuadroApellido,cuadroDirección,textoComentario))
botonUPDATE.grid(row=6,column=2,padx=5,pady=5)

botonDELETE=Button(miFrame, text="DELETE",command=borrar)
botonDELETE.grid(row=6,column=3,padx=5,pady=5)


raiz.mainloop()