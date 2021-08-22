from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=500)

miFrame.pack()

#imagenes
miImagen=PhotoImage(file="D:\Python\graficos\pic2.png")

Label(miFrame,image=miImagen).place(x=100, y=209)

#creacion de labels de texto, #fg color letra, #font fuente
miLabel=Label(miFrame,text="HOLA PUTOS", fg="green", font=("Times New Roman",24))#contenedor padre, texto
#miLabel.pack() #esto hace que el contenedor se aplaque a las dimensiones del texto
miLabel.place(x=0, y=0) #con esto respeta el tamaño que le asigné a la raiz y me ubica el texto 

#modo abreviado, si no se desean variables tipo label
Label(miFrame,text="HOLA PUTOS").place(x=0, y=0)


root.mainloop()