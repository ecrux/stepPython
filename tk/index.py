from tkinter import  *

root = Tk() #Raiz
root.title("First Step")
# root.iconbitmap("icon.ico") #esto es para el icono
# root.resizable(False, False) para permitir o no cambiar de tamaño de la ventana

frame = Frame(root)
frame.pack()
frame.config(width=480, height=480)
frame.config(cursor="pirate", bg="blue")
root.mainloop() #Creamos la interfax


