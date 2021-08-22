from tkinter import *

root=Tk()

root.title("E")

A=IntVar()
B=IntVar()
C=IntVar()

def opcion():
    opcionEscogida=""

    if(A.get()==1):
        opcionEscogida+= "A"
    if(B.get()==1):
        opcionEscogida+= "B"
    if(C.get()==1):
        opcionEscogida+= "C"

    textoFinal.config(text=opcionEscogida)

foto=PhotoImage(file="D:\Python\P1.png")
Label(root, image=foto).pack()

miFrame=Frame(root)
miFrame.pack()

Label(miFrame, text="Elige", width=50).pack()

Checkbutton(miFrame, text="A", variable=A, onvalue=1, offvalue=0,command=opcion).pack()#Onvalue me determina el valor que tiene el boton cuando esté seleccionado
Checkbutton(miFrame, text="B",variable=B, onvalue=1, offvalue=0, command=opcion).pack()
Checkbutton(miFrame, text="C",variable=C, onvalue=1, offvalue=0, command=opcion).pack()

textoFinal=Label(miFrame)
textoFinal.pack()

root.mainloop()