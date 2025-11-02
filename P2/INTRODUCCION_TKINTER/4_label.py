from tkinter import *

ventana=Tk()

ventana.geometry("600x400")
ventana.title("Uso de Etiquetas o Label")

marco1=Frame(ventana,width=600,height=50,bg="#1BDCE3",relief="groove",border=4)
marco1.pack_propagate(False)
marco1.pack()
marco2=Frame(ventana,width=600,height=50,bg="#1BE36E",relief="groove",border=4)
marco2.pack_propagate(False)
marco2.pack()
marco3=Frame(ventana,width=600,height=50,bg="#F577E8",relief="groove",border=4).pack()
marco4=Frame(ventana,width=600,height=50,bg="#EF9764",relief="groove",border=4).pack()

# Etiquetas o Label

etiqueta1=Label(marco1,text="Alondra Abigail Sánchez",bg="#1BDCE3").pack()
etiqueta2=Label(marco2,text="Universidad Tecnologica de Durango").pack()
etiqueta3=Label(marco3,text="Tecnologias de la Información").pack()
etiqueta4=Label(marco4,text="Desarrollo de Software Multiplataforma").pack()

ventana.mainloop()
