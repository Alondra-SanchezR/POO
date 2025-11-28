from controller import funciones
from tkinter import *
from model import operaciones
from tkinter import messagebox

#Interfaz o View

class Vistas:
    def __init__(self,ventana):
        ventana.title("...Calculadora Básica...")
        ventana.geometry("500x400")
        ventana.resizable(False,False)
        self.interfaz(ventana)

    def interfaz(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        n1=IntVar()
        n2=IntVar()
        txt_numero1=Entry(ventana,textvariable=n1,width=5,justify="right")
        txt_numero1.focus()
        txt_numero1.pack(pady=5)

        txt_numero2=Entry(ventana,textvariable=n2,width=5,justify="right")
        txt_numero2.pack(pady=5)

        btn_suma=Button(ventana,text="+",command=lambda: funciones.Controladores.operaciones("Suma",n1.get(),n2.get(),"+"))
        btn_suma.pack()

        btn_resta=Button(ventana,text="-",command=lambda: funciones.Controladores.operaciones("Resta",n1.get(),n2.get(),"-"))
        btn_resta.pack()

        btn_multiplicacion=Button(ventana,text="x",command=lambda: funciones.Controladores.operaciones("Multiplicacion",n1.get(),n2.get(),"x"))
        btn_multiplicacion.pack()
        
        btn_division=Button(ventana,text="/",command=lambda: funciones.Controladores.operaciones("Division",n1.get(),n2.get(),"/"))
        btn_division.pack()

        btn_salir=Button(ventana,text="Salir",command=ventana.quit)
        btn_salir.pack(pady=10)

    def menuPrincipal(self,ventana):
        menuBar= Menu(ventana)
        ventana.config(menu=menuBar)
        archivoMenu=Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Operaciónes", menu=archivoMenu)
        archivoMenu.add_command(label="Agregar",command=lambda: self.interfaz(ventana))
        archivoMenu.add_command(label="Consultar",command=lambda: self.consultar(ventana))
        archivoMenu.add_command(label="Cambiar",command=lambda: self.cambiar(ventana))
        archivoMenu.add_command(label="Borrar",command=lambda: self.eliminar(ventana))
        archivoMenu.add_separator()
        archivoMenu.add_command(label="Salir", command=ventana.quit)
    
    def consultar(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        label_titulo=Label(ventana, text=".::Lista de las Operaciónes::.") 
        label_titulo.pack(pady=5)
        label_titulo.config()

        resultado = funciones.Controladores.consultar()
        if len(resultado)>0:
            n = 1
            for fila in resultado:
                texto = f"Operacion: {n}  ID:{fila[0]}  Fecha de creacion: {fila[1]} \nOperación: {fila[2]}{fila[4]}{fila[3]}={fila[5]}"
                label_item = Label(ventana, text=texto)
                label_item.pack()
                label_item.config()
                n += 1
        else:
            messagebox.showinfo(text="No existen operaciónes en el Sistema ... agregar operaciones ...")

        boton_volver=Button(ventana, text="Volver", command=lambda: self.interfaz(ventana))
        boton_volver.pack()

    def cambiar(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        label_titulo=Label(ventana, text=".::Lista de las Operaciónes::.") 
        label_titulo.pack(pady=5)
        label_titulo.config()

        label_id=Label(ventana, text="ID de la Operación: ")
        label_id.pack(pady=5)
        label_id.config()
        id = IntVar()
        entry_id=Entry(ventana, textvariable=id, justify="right",width=30)
        entry_id.focus()
        entry_id.pack(pady=5)

        label_num1=Label(ventana, text="Nuevo Número 1")
        label_num1.pack(pady=5)
        label_num1.config()
        num1 = IntVar()
        entry_num1=Entry(ventana, textvariable=num1, justify="right",width=30)
        entry_num1.pack(pady=5)

        label_num2=Label(ventana, text="Nuevo Número 2")
        label_num2.pack(pady=5)
        label_num2.config()
        num2 = IntVar()
        entry_num2=Entry(ventana, textvariable=num2, justify="right",width=30)
        entry_num2.pack(pady=5)

        label_signo=Label(ventana, text="Nuevo Signo")
        label_signo.pack(pady=5)
        label_signo.config()
        signo = StringVar()
        entry_signo=Entry(ventana, textvariable=signo, justify="right",width=30)
        entry_signo.pack(pady=5)

        label_resultado=Label(ventana, text="Nuevo Resultado")
        label_resultado.pack(pady=5)
        label_resultado.config()
        resultado = StringVar()
        entry_resultado=Entry(ventana, textvariable=resultado, justify="right",width=30)
        entry_resultado.pack(pady=5)

        boton_guardar=Button(ventana, text="Guardar", command=lambda: funciones.Controladores.cambiar(num1.get(), num2.get(), signo.get(), resultado.get(), id.get()))
        boton_guardar.pack(pady=10)

        boton_volver=Button(ventana, text="Volver", command=lambda: self.interfaz(ventana))
        boton_volver.pack()

    def eliminar(self,ventana):
        self.borrarPantalla(ventana)
        self.menuPrincipal(ventana)
        label_titulo=Label(ventana, text=".::Borrar una Operación::.")
        label_titulo.pack(pady=5)
        label_titulo.config(
        font=("Arial", 18)
        )

        label_id=Label(ventana, text="ID de la Operación: ")
        label_id.pack(pady=5)
        label_id.config(
        font=("Arial", 12)
        )

        id = IntVar()
        entry_id=Entry(ventana, textvariable=id, justify="right",width=5)
        entry_id.focus()
        entry_id.pack(pady=5)

        boton_eliminar=Button(ventana, text="Eliminar", command=lambda: funciones.Controladores.eliminar(id.get()))
        boton_eliminar.pack()

        boton_volver=Button(ventana, text="Volver", command=lambda: self.interfaz(ventana))
        boton_volver.pack()
    
    def borrarPantalla(self,ventana):
        for widget in ventana.winfo_children():
            widget.destroy()