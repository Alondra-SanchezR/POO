from model import cochesBD
from controller import coches
import os
import tkinter as tk
from tkinter import messagebox

class Menu:
    def __init__(self, ventana):
        ventana.geometry("1000x750")
        ventana.resizable(False, False)
        self.main(ventana)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def main(self, ventana):
        #Borrar pantalla
        self.borrarPantalla(ventana)

        #funciones
        def salida(ventana):
            salir=messagebox.showinfo(title="Saliendo del programa", message="¡Gracias por utilizar el sistema!")
            ventana.quit()

        #titulo    
        lbl_titulo=tk.Label(ventana, text=".:: Menu Principal ::.\n\nElige un opción: ")
        lbl_titulo.pack(pady=[10,15])

        #botones
        btn_autos=tk.Button(ventana, text="Autos", command=lambda:self.menu_acciones(ventana, "autos"))
        btn_autos.config(width=12)
        btn_autos.pack(pady=10)

        btn_camionetas=tk.Button(ventana, text="Camionetas", command=lambda:self.menu_acciones(ventana, "camionetas"))
        btn_camionetas.config(width=12)
        btn_camionetas.pack(pady=10)

        btn_camiones=tk.Button(ventana, text="Camiones", command=lambda:self.menu_acciones(ventana, "camiones"))
        btn_camiones.config(width=12)
        btn_camiones.pack(pady=[10,15])

        btn_salir=tk.Button(ventana, text="Salir", command=lambda:salida(ventana))
        btn_salir.config(width=10)
        btn_salir.pack(pady=15)

    def menu_acciones(self,ventana,tipo):
        #Borrar pantalla
        self.borrarPantalla(ventana)

        #titulo    
        lbl_titulo=tk.Label(ventana, text=f".:: Menu de {tipo} ::.")
        lbl_titulo.pack(pady=[10,15])

        #botones
        btn_insert=tk.Button(ventana, text="Insertar", command=lambda:self.menu_agregar(ventana, tipo))
        btn_insert.config(width=12)
        btn_insert.pack(pady=10)

        btn_consult=tk.Button(ventana, text="Consultar", command=lambda:self.menu_camionetas(ventana))
        btn_consult.config(width=12)
        btn_consult.pack(pady=10)

        btn_actual=tk.Button(ventana, text="Actualizar", command=lambda:self.menu_camiones(ventana))
        btn_actual.config(width=12)
        btn_actual.pack(pady=[10,15])

        btn_elimin=tk.Button(ventana, text="Eliminar", command=lambda:self.menu_camiones(ventana))
        btn_elimin.config(width=12)
        btn_elimin.pack(pady=[10,15])

        btn_return=tk.Button(ventana, text="Regresar", command=lambda:self.main(ventana))
        btn_return.config(width=10)
        btn_return.pack(pady=15)

    def menu_agregar(self, ventana, tipo):
        #Borrar Pantalla
        self.borrarPantalla(ventana)
    
        #Variables
        marca=tk.StringVar()
        color=tk.StringVar()
        colores=["azul","negro","rojo","verde","amarillo","blanco","gris","celeste","naranja"]
        color.set(colores[0])
        modelo=tk.StringVar()
        velocidad=tk.StringVar()
        potencia=tk.IntVar()
        plazas=tk.IntVar()
        if tipo=="autos":
            extra1="0"
            extra2="0"
        elif tipo=="camionetas":
            extra1=tk.StringVar()
            tracciones=["delantera","trasera","dual"]
            extra1.set(tracciones[0])
            extra2=tk.BooleanVar()
        elif tipo=="camiones":
            extra1=tk.IntVar()
            extra2=tk.IntVar()

        #limitar las cajas de texto
        def limit_float(p):
            allowed = "0123456789."
            if all(ch in allowed for ch in p) and p.count(".") <= 1:
                return True
            else:
                return False

        def limit_int(p):
            if p.isdigit():
                return True
            else:
                return False

        verificacion_entero=(ventana.register(limit_int), "%P")    
        verificacion_real=(ventana.register(limit_float), "%P")

        #Funciones
        def agregar(tipo,nombre,color,modelo,velocidad,potencia,plaza,extra1,extra2):
            dato=coches.funciones.insertar_vehiculo(tipo,nombre,color,modelo,velocidad,potencia,plaza,extra1,extra2)
            if dato:
                self.menu_acciones(ventana, tipo)

        #Título
        lbl_titulo=tk.Label(ventana, text=f"Ingresa los siguientes datos del vehículo de tipo {tipo}")
        lbl_titulo.pack(pady=[15,25])

        #marca del vehículo
        lbl_marca=tk.Label(ventana, text="Marca: ", justify="left")
        lbl_marca.pack(pady=5)

        txt_marca=tk.Entry(ventana, textvariable=marca)
        txt_marca.pack(pady=[0,15])

        #color del vehículo
        lbl_color=tk.Label(ventana, text="Color: ", justify="left")
        lbl_color.pack(pady=5)

        opt_color=tk.OptionMenu(ventana, color, *colores)
        opt_color.pack(pady=[0,15])

        #modelo del vehículo
        lbl_modelo=tk.Label(ventana, text="Modelo: ", justify="left")
        lbl_modelo.pack(pady=5)

        txt_modelo=tk.Entry(ventana, textvariable=modelo)
        txt_modelo.pack(pady=[0,15])

        #velocidad del vehículo
        lbl_vel=tk.Label(ventana, text="Velocidad: ", justify="left")
        lbl_vel.pack(pady=5)

        txt_vel=tk.Entry(ventana, textvariable=velocidad, validate="key", validatecommand=verificacion_real)
        txt_vel.pack(pady=[0,15])
        
        #potencia del vehículo
        lbl_poten=tk.Label(ventana, text="Potencia: ", justify="left")
        lbl_poten.pack(pady=5)

        txt_poten=tk.Entry(ventana, textvariable=potencia, validate="key", validatecommand=verificacion_entero)
        txt_poten.pack(pady=[0,15])

        #plazas del vehículo
        lbl_plaza=tk.Label(ventana, text="Plazas: ", justify="left")
        lbl_plaza.pack(pady=5)

        txt_plaza=tk.Entry(ventana, textvariable=plazas, validate="key", validatecommand=verificacion_entero)
        txt_plaza.pack(pady=[0,15])

        if tipo=="camionetas":
            #traccion de la camioneta
            lbl_extra1=tk.Label(ventana, text="Traccion: ", justify="left")
            lbl_extra1.pack(pady=5)

            opt_extra1=tk.OptionMenu(ventana, extra1, *tracciones)
            opt_extra1.pack(pady=[0,15])

            #estatus de la camioneta
            chk_extra2=tk.Checkbutton(ventana, text="¿Se encuentra cerrada?", variable=extra2, onvalue=True, offvalue=False)
            chk_extra2.pack(pady=[5,15])
        elif tipo=="camiones":
            #ejes del camion
            lbl_eje=tk.Label(ventana, text="Ejes: ", justify="left")
            lbl_eje.pack(pady=5)

            txt_eje=tk.Entry(ventana, textvariable=extra1, validate="key", validatecommand=verificacion_entero)
            txt_eje.pack(pady=[0,15])

            #capacidad de carga del camion
            lbl_eje=tk.Label(ventana, text="Capacidad de carga: ", justify="left")
            lbl_eje.pack(pady=5)

            txt_eje=tk.Entry(ventana, textvariable=extra2, validate="key", validatecommand=verificacion_entero)
            txt_eje.pack(pady=[0,15])

        #botones
        btn_entrar=tk.Button(ventana, text="Entrar", command=lambda:agregar(tipo, marca.get(), color.get(), modelo.get(), velocidad.get(), potencia.get(), plazas.get(), extra1.get(), extra2.get()))
        btn_entrar.config(
            width=12
        )
        btn_entrar.pack(pady=10)

        btn_volver=tk.Button(ventana, text="Volver", command=lambda:self.menu_acciones(ventana, tipo))
        btn_volver.config(
            width=12
        )
        btn_volver.pack(pady=10)