from tkinter import *

ventana=Tk()

ventana.title("Personalizar widegts u objetos")
ventana.geometry("500x500")

etiqueta=Label(ventana,text="Bienvenidos a Tkinter")
etiqueta.config(
    bg="lightblue",
    fg="darkblue",
    width=50,
    height=4,
    font=("Helvetica",30,"italic"),
    border=3,
    relief="solid"
)
etiqueta.pack(pady=15)

boton1=Button(ventana,text="Haz Clic ...")
boton1.config(
    bg="blue",
    fg="white",
    width=15,
    font=("Arial",20,"bold"),
    relief=GROOVE,
    border=2,
    activebackground="red",
    activeforeground="yellow",
)
boton1.pack(pady=15)

boton2=Button(ventana,text="Regresar Valores ...",command="")
boton2.config(
    fg="black",
    width=15,
    font=("Arial",20,"bold"),
    relief=GROOVE,
    border=2,
    activebackground="grey",
)
boton2.pack(pady=15)

ventana.mainloop()