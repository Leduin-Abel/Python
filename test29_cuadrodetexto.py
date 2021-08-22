from tkinter import *

raiz=Tk()

miFrame=Frame(raiz,width=1200, height=200)
miFrame.pack()

minombre=StringVar()#le avisa al piton que es una cadera de caracteres


#cuadro de texto de entrada
cuadroNombre=Entry(miFrame, textvariable=minombre)#se asocia el valor del cuadro con el de la variable
#cuadroTexto.place(x=100,y=100)
#utilizando grid

cuadroNombre.grid(row=0,column=1,padx=5,pady=5)#le entra fila y columna, inicia desde 0

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1,column=1,padx=5,pady=5)
cuadroPass.config(show="¬")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1,padx=5,pady=5)

cuadroDirección=Entry(miFrame)
cuadroDirección.grid(row=3,column=1,padx=5,pady=5)

#TEXT
textoComentario=Text(miFrame, width=16, height=4)#cuadro auto extendible
textoComentario.grid(row=4,column=1,padx=5,pady=5)
barravert=Scrollbar(miFrame,command=textoComentario.yview)#barra de scroll, command=,,,,.yview para que vaya vertical
barravert.grid(row=4,column=2,sticky="nsew")#para agregarlo al cuadrotext, nsew permite que se adapte al tamaño del widget
textoComentario.config(yscrollcommand=barravert.set)#la barra sigue la posición del texto


#Labels
#sticky me permite determinar como van alineados los textos, va con los cardinales en ingles
nombreLabel=Label(miFrame,text="Nombre:")
#nombreLabel.place(x=120, y=100)
#utilizando grid
nombreLabel.grid(row=0,column=0, sticky="e",padx=5,pady=5)#le entra fila y columna, inicia desde 0


passLabel=Label(miFrame,text="Contraseña:")
passLabel.grid(row=1,column=0,sticky="e",padx=5,pady=5)

#padx y pady son espaciados
apellidoLabel=Label(miFrame,text="Apellido: ")
apellidoLabel.grid(row=2,column=0,sticky="e",padx=5,pady=5)



direccionLabel=Label(miFrame,text="Dirección:")
direccionLabel.grid(row=3,column=0,sticky="e",padx=5,pady=5)

comentariosLabel=Label(miFrame,text="Contraseña:")
comentariosLabel.grid(row=4,column=0,sticky="e",padx=5,pady=5)

#botonessss

def codigoBoton():
    minombre.set("Abel")

botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()
 

raiz.mainloop()