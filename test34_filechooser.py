from tkinter import *
from tkinter import filedialog

root=Tk()

def abreFichero():
    fichero=filedialog.askopenfilename(title="Abrir",initialdir="C:", filetypes=(("O de Excel", "*.xlsx"),
    ("Ficheros de texto", "*.txt"), ("TODO", "*.*")))#initialdir es la direccion inicial; #filetypes=filtros de tipp de archivo

    print(fichero)

Button(root,text="Abrir",command=abreFichero).pack()

root.mainloop()