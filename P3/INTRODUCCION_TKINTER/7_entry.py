from tkinter import *

ventana=Tk()
ventana.title("...Acceso al Sistema...")
ventana.geometry("500x500")

lbl_nombre=Label(ventana,text="Nombre")
lbl_nombre.pack()

txt_nombre=Entry(ventana,width=55)
txt_nombre.pack()

lbl_password=Label(ventana,text="Contraseña")
lbl_password.pack()

txt_password=Entry(ventana,width=55)
txt_password.pack()

btn_aceptar=Button(ventana,text="Aceptar")
btn_aceptar.pack()

btn_borrar=Button(ventana,text="Borrar")
btn_borrar.pack()

ventana.mainloop()




#def cambiar():
#    lbl_resultado.config(text=f"Bienvenido ... {nombre.get()}")
#ventana=Tk()
#ventana.title("Entry")
#ventana.geometry("500x500")
#lbl_nombre=Label(ventana,text="Ingrese su nombre ...").pack()
#nombre=StringVar()
#txt_nombre=Entry(ventana,textvariable=nombre,width=55)
#txt_nombre.pack()
#btn_saludar=Button(ventana,text="Saludar",command=cambiar)
#btn_saludar.pack()
#lbl_resultado=Label(ventana,text="")
#lbl_resultado.pack()
#ventana.mainloop()