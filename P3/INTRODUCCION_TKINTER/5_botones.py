from tkinter import *

def cambiarTexto():
    label_nombre.config(text="Alondra")
    label_password.config(text="1234")

def regresarTexto():
    label_nombre.config(text="Nombre: ....")
    label_password.config(text="Contraseña: ...")

ventana=Tk()

ventana.title("Uso de Botones, Marcos, Etiquetas")
ventana.geometry("800x600")

frame_principal=Frame(ventana)
frame_principal.config(
    width=800,
    height=100,
    bg="#6DECD1",
    relief="solid",
    border=3
)
frame_principal.pack_propagate(False)
frame_principal.pack(pady=10)

label_titulo=Label(frame_principal)
label_titulo.config(
    text="Inicio de Sesión",
    bg="#6DECD1",
    height=50
)
label_titulo.pack()

label_nombre=Label(ventana,text="Nombre...")
label_nombre.pack(pady=10)
label_password=Label(ventana,text="Contraseña...")
label_password.pack(pady=10)

btn_aceptar=Button(ventana,text="Aceptar",command=cambiarTexto).pack(pady=10)
btn_ingresar=Button(ventana,text="Ingresar",command=regresarTexto).pack(pady=10)

ventana.mainloop()