from tkinter import *

root=Tk()

def imprimir():
   # print(varOpcion.get()) #1 o 2 en consola
    if varOpcion.get()==1:
       etiqueta.config(text="A")
    elif varOpcion.get()==2:
        etiqueta.config(text="B")
    else:
        etiqueta.config(text="C")


varOpcion=IntVar()
Label(root, text="Opción").pack()
Radiobutton(root, text="A",variable=varOpcion, value=1, command=imprimir).pack()#igual que con stringvar
Radiobutton(root, text="B", variable=varOpcion, value=2,command=imprimir).pack()
Radiobutton(root, text="C", variable=varOpcion, value=3,command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()


root.mainloop()