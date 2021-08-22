from tkinter import *
from tkinter import messagebox #ventanas emergentes

root=Tk()
def infoAddicional():
    messagebox.showinfo("AAAAAAAAAAAAAA","BBBBBBBBBBBB")#Le entra el titulo de la ventana y lo que dice la ventana

def avisoLicencia():
    messagebox.showwarning("ASDASDas","AAAA")

def salirAplicacion():
    #valor=messagebox.askquestion("Salir", "¿Se quiere ir maquina?")#devuelve yes or no
    valor=messagebox.askokcancel("Salir", "¿Se quiere ir maquina?")#devuelve true or false
    if valor==True:
        root.destroy()

def cerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar", "Yaper")
    if valor==False:
        root.destroy()


barraMenu=Menu(root)
root.config(menu=barraMenu,width=300, height=300)

archivoMenu=Menu(barraMenu,tearoff=0) #tearoff le quitan el separador
#submenu
archivoMenu.add_command(label="nuevo")
archivoMenu.add_command(label="guardar")
archivoMenu.add_command(label="guaardar como")
archivoMenu.add_separator()#separador
archivoMenu.add_command(label="cerrr",command=cerrarDocumento)
archivoMenu.add_command(label="salir", command=salirAplicacion)

archivoEdicion=Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label="copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="pegar")

archivoHerramientas=Menu(barraMenu,tearoff=0)

archivoAyuda=Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="livemcia",command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAddicional)


#menu
barraMenu.add_cascade(label="Archivo", menu=archivoMenu) 
barraMenu.add_cascade(label="Edición", menu=archivoEdicion) 
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas) 
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda) 



root.mainloop()