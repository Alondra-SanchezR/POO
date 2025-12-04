from tkinter import *
from tkinter import messagebox


class Menu():
    def __init__(self,ventana):
        ventana.geometry("800x600")
        ventana.title("Coches system")
        self.menu_principal(ventana)

    def borrarPantalla(self,ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def menu_principal(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=".:: Menu principal ::.")
        lblTitulo.pack(pady=5)
        btnCoches=Button(ventana,text="1.- Coches",command=lambda : self.menu_acciones(ventana,"coches"))
        btnCoches.pack(pady=5)
        btnCamiones=Button(ventana,text="2.- Camiones",command=lambda: self.menu_acciones(ventana,"camiones"))
        btnCamiones.pack(pady=5)
        btnCamionetas=Button(ventana,text="3.- Camionetas",command=lambda: self.menu_acciones(ventana,"camionetas"))
        btnCamionetas.pack(pady=5)
        btnSalir=Button(ventana,text="4.- Salir",command=ventana.quit)
        btnSalir.pack(pady=5)

    def menu_acciones(self,ventana,vehiculo):
        global tipo
        tipo=vehiculo
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text=f"Menu de {tipo}")
        lblTitulo.pack(pady=5)
        btnAgregar=Button(ventana,text="1.-Agregar",command=lambda: self.insertar_autos(ventana))
        btnAgregar.pack(pady=5)
        btnMostrar=Button(ventana,text="2.-Mostrar",command=lambda: self.consultar_autos(ventana))
        btnMostrar.pack(pady=5)
        btnCambiar=Button(ventana,text="3.-Cambiar",command=lambda: self.cambiar_autos(ventana))
        btnCambiar.pack(pady=5)
        btnEliminar=Button(ventana,text="4.-Eliminar",command=lambda: self.borrar_autos(ventana))
        btnEliminar.pack(pady=5)
        btnSalir=Button(ventana,text="5.-Volver",command=lambda: self.menu_principal(ventana))
        btnSalir.pack(pady=5)
    
    def agregar_tipo(self,ventana,tipo):
        if tipo == "coches":
            self.insertar_autos(ventana)
        elif tipo == "camionetas":
            self.insertar_camiones(ventana)
        elif tipo == "camiones":
            self.insertar_camionetas(ventana)


#Tipo: Autos/Coches
    def insertar_autos(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Agregar coches")
        lblTitulo.pack(pady=5)
        lblMarca=Label(ventana,text="Inserte la marca")
        lblMarca.pack()
        txtMarca=Entry(ventana)
        txtMarca.pack(pady=5)

        lblColor=Label(ventana,text="Inserte el color")
        lblColor.pack()
        txtColor=Entry(ventana)
        txtColor.pack(pady=5)

        lblModelo=Label(ventana,text="Inserte el modelo")
        lblModelo.pack()
        txtModelo=Entry(ventana)
        txtModelo.pack(pady=5)

        lblVelocidad=Label(ventana,text="Inserte la velocidad")
        lblVelocidad.pack()
        txtVelocidad=Entry(ventana)
        txtVelocidad.pack(pady=5)

        lblPotencia=Label(ventana,text="Inserte la potencia")
        lblPotencia.pack()
        txtPotencia=Entry(ventana)
        txtPotencia.pack(pady=5)

        lblPlazas=Label(ventana,text="Inserte las plazas")
        lblPlazas.pack()
        txtPlazas=Entry(ventana)
        txtPlazas.pack(pady=5)

        btnAgregar=Button(ventana,text="Agregar",command= lambda: "")
        btnAgregar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    def consultar_autos(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Coches agregados")
        lblTitulo.pack(pady=5)
        filas=""
        registros=[("1","Honda","Gris","2020","180","400","4"),("2","BMW","Rojo","2023","250","400","2")]
        if len(registros)>0:
          num_autos=1
          for fila in registros:
            filas=filas+f"\nAuto #{num_autos} con ID: {fila[0]} \nMarca: {fila[1]} Color: {fila[2]} Modelo: {fila[3]} Velocidad: {fila[4]} Potencia: {fila[5]} Plazas: {fila[6]}"
            num_autos+=1
        else:
            messagebox.showinfo(message="No existen coches en el sistema")

        lblNota=Label(ventana,text=filas)
        lblNota.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command=lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    def cambiar_autos(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Cambiar coche")
        lblTitulo.pack(pady=5)

        lblId=Label(ventana,text="Ingrese el id")
        lblId.pack(pady=5)
        txtId=Entry(ventana)
        txtId.pack()

        lblMarca=Label(ventana,text="Inserte la marca")
        lblMarca.pack()
        txtMarca=Entry(ventana)
        txtMarca.pack(pady=5)

        lblColor=Label(ventana,text="Inserte el color")
        lblColor.pack()
        txtColor=Entry(ventana)
        txtColor.pack(pady=5)

        lblModelo=Label(ventana,text="Inserte el modelo")
        lblModelo.pack()
        txtModelo=Entry(ventana)
        txtModelo.pack(pady=5)

        lblVelocidad=Label(ventana,text="Inserte la velocidad")
        lblVelocidad.pack()
        txtVelocidad=Entry(ventana)
        txtVelocidad.pack(pady=5)

        lblPotencia=Label(ventana,text="Inserte la potencia")
        lblPotencia.pack()
        txtPotencia=Entry(ventana)
        txtPotencia.pack(pady=5)

        lblPlazas=Label(ventana,text="Inserte las plazas")
        lblPlazas.pack()
        txtPlazas=Entry(ventana)
        txtPlazas.pack(pady=5)

        btnGuardar=Button(ventana,text="Guardar",command= lambda: "")
        btnGuardar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    def borrar_autos(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Eliminar un coche")
        lblTitulo.pack(pady=5)
        lblId=Label(ventana,text="Ingrese el id")
        lblId.pack(pady=5)
        txtId=Entry(ventana)
        txtId.pack()
        btnEliminar=Button(ventana,text="Eliminar",command= lambda:"")
        btnEliminar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

#Tipo: Camionetas
    def insertar_camionetas(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Agregar camionetas")
        lblTitulo.pack(pady=5)
        lblMarca=Label(ventana,text="Inserte la marca")
        lblMarca.pack()
        txtMarca=Entry(ventana)
        txtMarca.pack(pady=5)

        lblColor=Label(ventana,text="Inserte el color")
        lblColor.pack()
        txtColor=Entry(ventana)
        txtColor.pack(pady=5)

        lblModelo=Label(ventana,text="Inserte el modelo")
        lblModelo.pack()
        txtModelo=Entry(ventana)
        txtModelo.pack(pady=5)

        lblVelocidad=Label(ventana,text="Inserte la velocidad")
        lblVelocidad.pack()
        txtVelocidad=Entry(ventana)
        txtVelocidad.pack(pady=5)

        lblCaballaje=Label(ventana,text="Inserte el caballaje")
        lblCaballaje.pack()
        txtCaballaje=Entry(ventana)
        txtCaballaje.pack(pady=5)

        lblPlazas=Label(ventana,text="Inserte las plazas")
        lblPlazas.pack()
        txtPlazas=Entry(ventana)
        txtPlazas.pack(pady=5)

        lblEje=Label(ventana,text="Inserte el eje")
        lblEje.pack()
        txtEje=Entry(ventana)
        txtEje.pack(pady=5)

        lblCapacidadCarga=Label(ventana,text="Inserte la capacidad de carga")
        lblCapacidadCarga.pack()
        txtCapacidadCarga=Entry(ventana)
        txtCapacidadCarga.pack(pady=5)

        btnAgregar=Button(ventana,text="Agregar",command= lambda: "")
        btnAgregar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)
    
    def consultar_camionetas(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Camionetas agregadas")
        lblTitulo.pack(pady=5)
        filas=""
        registros=[("1","Ford","Negro","2020","180","300","4","2","5000"),
            ("2","Chevrolet","Blanco","2021","200","350","4","2","6000")]
        if len(registros)>0: 
            num_vehiculos=1
            for fila in registros:
                filas=filas+f"\nCamioneta #{num_vehiculos} con ID: {fila[0]} \nMarca: {fila[1]} Color: {fila[2]} Modelo: {fila[3]} Velocidad: {fila[4]} Caballaje: {fila[5]} Plazas: {fila[6]} Eje: {fila[7]} Capacidad de Carga: {fila[8]}"
                num_vehiculos+=1
        else:
            messagebox.showinfo(message="No existen camionetas en el sistema") 

        lblNota=Label(ventana,text=filas)
        lblNota.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command=lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)       
    
    def cambiar_camionetas(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Cambiar camioneta")
        lblTitulo.pack(pady=5)

        lblId=Label(ventana,text="Ingrese el id")
        lblId.pack(pady=5)
        txtId=Entry(ventana)
        txtId.pack()

        lblMarca=Label(ventana,text="Inserte la marca")
        lblMarca.pack()
        txtMarca=Entry(ventana)
        txtMarca.pack(pady=5)

        lblColor=Label(ventana,text="Inserte el color")
        lblColor.pack()
        txtColor=Entry(ventana)
        txtColor.pack(pady=5)

        lblModelo=Label(ventana,text="Inserte el modelo")
        lblModelo.pack()
        txtModelo=Entry(ventana)
        txtModelo.pack(pady=5)

        lblVelocidad=Label(ventana,text="Inserte la velocidad")
        lblVelocidad.pack()
        txtVelocidad=Entry(ventana)
        txtVelocidad.pack(pady=5)

        lblCaballaje=Label(ventana,text="Inserte el caballaje")
        lblCaballaje.pack()
        txtCaballaje=Entry(ventana)
        txtCaballaje.pack(pady=5)

        lblPlazas=Label(ventana,text="Inserte las plazas")
        lblPlazas.pack()
        txtPlazas=Entry(ventana)
        txtPlazas.pack(pady=5)

        lblEje=Label(ventana,text="Inserte el eje")
        lblEje.pack()
        txtEje=Entry(ventana)
        txtEje.pack(pady=5)

        lblCapacidadCarga=Label(ventana,text="Inserte la capacidad de carga")
        lblCapacidadCarga.pack()
        txtCapacidadCarga=Entry(ventana)
        txtCapacidadCarga.pack(pady=5)

        btnGuardar=Button(ventana,text="Guardar",command= lambda: "")
        btnGuardar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    def borrar_camionetas(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Eliminar una camioneta")
        lblTitulo.pack(pady=5)
        lblId=Label(ventana,text="Ingrese el id")
        lblId.pack(pady=5)
        txtId=Entry(ventana)
        txtId.pack()
        btnEliminar=Button(ventana,text="Eliminar",command= lambda:"")
        btnEliminar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

#Tipo: Camiones
    def insertar_camiones(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Agregar camiones")
        lblTitulo.pack(pady=5)
        lblMarca=Label(ventana,text="Inserte la marca")
        lblMarca.pack()
        txtMarca=Entry(ventana)
        txtMarca.pack(pady=5)

        lblColor=Label(ventana,text="Inserte el color")
        lblColor.pack()
        txtColor=Entry(ventana)
        txtColor.pack(pady=5)

        lblModelo=Label(ventana,text="Inserte el modelo")
        lblModelo.pack()
        txtModelo=Entry(ventana)
        txtModelo.pack(pady=5)

        lblVelocidad=Label(ventana,text="Inserte la velocidad")
        lblVelocidad.pack()
        txtVelocidad=Entry(ventana)
        txtVelocidad.pack(pady=5)

        lblCaballaje=Label(ventana,text="Inserte el caballaje")
        lblCaballaje.pack()
        txtCaballaje=Entry(ventana)
        txtCaballaje.pack(pady=5)

        lblPlazas=Label(ventana,text="Inserte las plazas")
        lblPlazas.pack()
        txtPlazas=Entry(ventana)
        txtPlazas.pack(pady=5)

        lblTraccion=Label(ventana,text="Inserte la tracción")
        lblTraccion.pack()
        txtTraccion=Entry(ventana)
        txtTraccion.pack(pady=5)

        lblCapacidadCarga=Label(ventana,text="Inserte la capacidad de carga")
        lblCapacidadCarga.pack()
        txtCapacidadCarga=Entry(ventana)
        txtCapacidadCarga.pack(pady=5)

        btnAgregar=Button(ventana,text="Agregar",command= lambda: "")
        btnAgregar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)
    
    def consultar_camiones(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Camiones agregados")
        lblTitulo.pack(pady=5)
        filas=""
        registros=[("3","Mercedes","Blanco","2022","115","480","2","6x4","30000"),
    ("4","Freightliner","Negro","2021","140","500","1","8x4","35000"),("5","Kenworth","Verde","2023","125","420","2","4x2","18000")]
        if len(registros)>0:
            num_vehiculos=1
            for fila in registros:
                filas=filas+f"\nCamión #{num_vehiculos} con ID: {fila[0]} \nMarca: {fila[1]} Color: {fila[2]} Modelo: {fila[3]} Velocidad: {fila[4]} Caballaje: {fila[5]} Plazas: {fila[6]} Tracción: {fila[7]} Capacidad de Carga: {fila[8]}"
                num_vehiculos+=1
        else:
            messagebox.showinfo(message="No existen camiones en el sistema")

        lblNota=Label(ventana,text=filas)
        lblNota.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command=lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)

    def cambiar_camiones(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Cambiar camión")
        lblTitulo.pack(pady=5)

        lblId=Label(ventana,text="Ingrese el id")
        lblId.pack(pady=5)
        txtId=Entry(ventana)
        txtId.pack()

        lblMarca=Label(ventana,text="Inserte la marca")
        lblMarca.pack()
        txtMarca=Entry(ventana)
        txtMarca.pack(pady=5)

        lblColor=Label(ventana,text="Inserte el color")
        lblColor.pack()
        txtColor=Entry(ventana)
        txtColor.pack(pady=5)

        lblModelo=Label(ventana,text="Inserte el modelo")
        lblModelo.pack()
        txtModelo=Entry(ventana)
        txtModelo.pack(pady=5)

        lblVelocidad=Label(ventana,text="Inserte la velocidad")
        lblVelocidad.pack()
        txtVelocidad=Entry(ventana)
        txtVelocidad.pack(pady=5)

        lblCaballaje=Label(ventana,text="Inserte el caballaje")
        lblCaballaje.pack()
        txtCaballaje=Entry(ventana)
        txtCaballaje.pack(pady=5)

        lblPlazas=Label(ventana,text="Inserte las plazas")
        lblPlazas.pack()
        txtPlazas=Entry(ventana)
        txtPlazas.pack(pady=5)

        lblTraccion=Label(ventana,text="Inserte la tracción")
        lblTraccion.pack()
        txtTraccion=Entry(ventana)
        txtTraccion.pack(pady=5)

        lblCapacidadCarga=Label(ventana,text="Inserte la capacidad de carga")
        lblCapacidadCarga.pack()
        txtCapacidadCarga=Entry(ventana)
        txtCapacidadCarga.pack(pady=5)

        btnGuardar=Button(ventana,text="Guardar",command= lambda: "")
        btnGuardar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)
    
    def borrar_camiones(self,ventana):
        self.borrarPantalla(ventana)
        lblTitulo=Label(ventana,text="Eliminar un camión")
        lblTitulo.pack(pady=5)
        lblId=Label(ventana,text="Ingrese el id")
        lblId.pack(pady=5)
        txtId=Entry(ventana)
        txtId.pack()
        btnEliminar=Button(ventana,text="Eliminar",command= lambda:"")
        btnEliminar.pack(pady=5)
        btnVolver=Button(ventana,text="Volver",command= lambda: self.menu_acciones(ventana,tipo))
        btnVolver.pack(pady=5)