from tkinter import *

raiz=Tk()


#titulo
raiz.title("Ventana de pruebas")

#permitir o negar el redimensionamiento
#raiz.resizable(1,0)#(ancho,alto) #1 permite 0 niega

#para cambiar el icono archivos.ico
#cambia del icono
raiz.iconbitmap("D:\Python\graficos\logo2.ico")#la dirección del archivo

#tamaño por defecto
#raiz.geometry("650x350")#ancho y alto

#configuración
raiz.config(bg="black")#bg es background

#creando frames
miframe=Frame()

#empaquetado
#miframe.pack(side="right")#se ancla al lado derecho

#miframe.pack(side="right", anchor="s") #anchor me permite mover el anclamiento, utiliza puntos cardinales en ingles

miframe.pack(fill="x", expand=True)#llenado, con esa combicación me permite llenar en y, fill=both en ambos

#personalizando el frame, tienen tamaño fijo
miframe.config(bg="red")

#La raiz se adapta al tamaño del frame por lo tanto solo es necesario el tamaño del frame
#asignación
miframe.config(width="650", height="350")

#todo lo config del frame se lo puedo aplicar a la raiz
#grosor bordes
miframe.config(bd="35")

#bordes especiales
miframe.config(relief="groove")

#modificar el cursor en el frame
miframe.config(cursor="pirate")

#mainloop siempre de estar de ultimo
raiz.mainloop()