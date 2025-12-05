from tkinter import *
from tkinter import messagebox
from controller import controlador

class VistaGestion():
    
    def __init__(self, ventana):
        ventana.geometry("800x600")
        ventana.title("Sistema de Gestión Coches")
        VistaGestion.cargar_menu_principal(ventana)

    @staticmethod
    def limpiar_interfaz(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def cargar_menu_principal(ventana):
        VistaGestion.limpiar_interfaz(ventana)
        
        lblHeader = Label(ventana, text=".::: Panel de Control :::.", font=("Arial", 14))
        lblHeader.pack(pady=10)
        
        btnAutos = Button(ventana, text="1. Autos", width=30, command=lambda: VistaGestion.cargar_submenu(ventana, "coches"))
        btnAutos.pack(pady=5)
        
        btnPesados = Button(ventana, text="2. Camiones", width=30, command=lambda: VistaGestion.cargar_submenu(ventana, "camiones"))
        btnPesados.pack(pady=5)
        
        btnPickups = Button(ventana, text="3. Camionetas", width=30, command=lambda: VistaGestion.cargar_submenu(ventana, "camionetas"))
        btnPickups.pack(pady=5)
        
        btnExit = Button(ventana, text="4. Salir", width=30, command=ventana.quit)
        btnExit.pack(pady=20)

    @staticmethod
    def cargar_submenu(ventana, categoria):
        global tipo_actual
        tipo_actual = categoria
        
        VistaGestion.limpiar_interfaz(ventana)
        
        lblHeader = Label(ventana, text=f"Administrando: {tipo_actual.upper()}", font=("Arial", 12, "bold"))
        lblHeader.pack(pady=10)

        if tipo_actual == "coches":
            btnNew = Button(ventana, text="Registrar Nuevo Auto", command=lambda: VistaGestion.vista_alta_coches(ventana))
            btnNew.pack(pady=5)
            btnShow = Button(ventana, text="Consultar", command=lambda: VistaGestion.vista_listar_coches(ventana))
            btnShow.pack(pady=5)
            
        elif tipo_actual == "camionetas":
            btnNew = Button(ventana, text="Registrar Nueva Camioneta", command=lambda: VistaGestion.vista_alta_camionetas(ventana))
            btnNew.pack(pady=5)
            btnShow = Button(ventana, text="Consultar", command=lambda: VistaGestion.vista_listar_camionetas(ventana))
            btnShow.pack(pady=5)
            
        elif tipo_actual == "camiones":
            btnNew = Button(ventana, text="Registrar Nuevo Camión", command=lambda: VistaGestion.vista_alta_camiones(ventana))
            btnNew.pack(pady=5)
            btnShow = Button(ventana, text="Consultar", command=lambda: VistaGestion.vista_listar_camiones(ventana))
            btnShow.pack(pady=5)

        btnEdit = Button(ventana, text="Modificar", command=lambda: VistaGestion.interfaz_busqueda_modificar(ventana))
        btnEdit.pack(pady=5)
        
        btnDel = Button(ventana, text="Eliminar", command=lambda: VistaGestion.interfaz_busqueda_eliminar(ventana))
        btnDel.pack(pady=5)
        
        btnBack = Button(ventana, text="Volver", command=lambda: VistaGestion.cargar_menu_principal(ventana))
        btnBack.pack(pady=20)


    @staticmethod
    def vista_alta_coches(ventana):
        VistaGestion.limpiar_interfaz(ventana)
        Label(ventana, text="Registro de Automóvil Nuevo", font=("Arial", 12)).pack(pady=10)

        Label(ventana, text="Marca:").pack()
        entry_fab = Entry(ventana)
        entry_fab.pack(pady=2)

        Label(ventana, text="Color:").pack()
        entry_color = Entry(ventana)
        entry_color.pack(pady=2)

        Label(ventana, text="Modelo:").pack()
        entry_mod = Entry(ventana)
        entry_mod.pack(pady=2)

        Label(ventana, text="Velocidad:").pack()
        entry_vel = Entry(ventana)
        entry_vel.pack(pady=2)

        Label(ventana, text="Caballaje:").pack()
        entry_pot = Entry(ventana)
        entry_pot.pack(pady=2)

        Label(ventana, text="Plazas:").pack()
        entry_plazas = Entry(ventana)
        entry_plazas.pack(pady=2)

        btnSave = Button(ventana, text="Guardar Registro", 
                         command=lambda: controlador.Controladores.insertar_coche(
                             entry_fab.get(), entry_color.get(), entry_mod.get(), 
                             entry_vel.get(), entry_pot.get(), entry_plazas.get()
                         ))
        btnSave.pack(pady=10)
        
        Button(ventana, text="Cancelar", command=lambda: VistaGestion.cargar_submenu(ventana, tipo_actual)).pack()

    @staticmethod
    def vista_listar_coches(ventana):
        VistaGestion.limpiar_interfaz(ventana)
        Label(ventana, text="Inventario de Coches", font=("Arial", 12)).pack(pady=10)
        
        texto_salida = ""
        registros = controlador.Controladores.mostrar_coche()
        contador = 1
        
        for item in registros:
            texto_salida += f"\nVehículo #{contador} | ID: {item[0]} \nMarca: {item[1]} | Color: {item[2]} | Modelo: {item[3]} | Velocidad: {item[4]} | Caballaje: {item[5]} | Plazas: {item[6]}"
            contador += 1
            
        lblData = Label(ventana, text=texto_salida, justify=LEFT)
        lblData.pack(pady=5)
        
        Button(ventana, text="Volver", command=lambda: VistaGestion.cargar_submenu(ventana, tipo_actual)).pack(pady=10)

    @staticmethod
    def vista_modificar_coche(ventana, opid):
        VistaGestion.limpiar_interfaz(ventana)
        Label(ventana, text="Modificar Automóvil", font=("Arial", 12)).pack(pady=10)

        Label(ventana, text="ID:").pack()
        var_id = IntVar()
        entry_id = Entry(ventana, textvariable=var_id)
        entry_id.delete(0, END)
        entry_id.insert(0, opid)
        entry_id.config(state="readonly")
        entry_id.pack()

        Label(ventana, text="Nueva Marca:").pack()
        e_fab = Entry(ventana)
        e_fab.pack(pady=2)

        Label(ventana, text="Nuevo Color:").pack()
        e_col = Entry(ventana)
        e_col.pack(pady=2)

        Label(ventana, text="Nuevo Modelo:").pack()
        e_mod = Entry(ventana)
        e_mod.pack(pady=2)

        Label(ventana, text="Nueva Velocidad:").pack()
        e_vel = Entry(ventana)
        e_vel.pack(pady=2)

        Label(ventana, text="Nuevo Caballaje:").pack()
        e_pot = Entry(ventana)
        e_pot.pack(pady=2)

        Label(ventana, text="Nuevas Plazas:").pack()
        e_pla = Entry(ventana)
        e_pla.pack(pady=2)

        btnUpdate = Button(ventana, text="Actualizar Datos", 
                           command=lambda: controlador.Controladores.actualizar_coche(
                               e_fab.get(), e_col.get(), e_mod.get(), 
                               e_vel.get(), e_pot.get(), e_pla.get(), var_id.get()
                           ))
        btnUpdate.pack(pady=10)
        Button(ventana, text="Cancelar", command=lambda: VistaGestion.cargar_submenu(ventana, tipo_actual)).pack()

    @staticmethod
    def vista_eliminar_coche(ventana, opid):
        VistaGestion.limpiar_interfaz(ventana)
        Label(ventana, text="Confirmar Eliminación", font=("Arial", 12, "bold"), fg="red").pack(pady=10)
        
        Label(ventana, text="ID a Eliminar:").pack(pady=5)
        var_id = IntVar()
        entry_id = Entry(ventana, textvariable=var_id)
        entry_id.delete(0, END)
        entry_id.insert(0, opid)
        entry_id.config(state="readonly")
        entry_id.pack()
        
        btnConfirm = Button(ventana, text="CONFIRMAR", bg="red", fg="white",
                            command=lambda: controlador.Controladores.eliminar_coche(var_id.get()))
        btnConfirm.pack(pady=10)
        Button(ventana, text="Cancelar", command=lambda: VistaGestion.cargar_submenu(ventana, tipo_actual)).pack()


    @staticmethod
    def vista_alta_camiones(ventana):
        VistaGestion.limpiar_interfaz(ventana)
        Label(ventana, text=f"Alta de {tipo_actual.capitalize()}", font=("Arial", 12)).pack(pady=10)

        Label(ventana, text="Marca:").pack()
        e_marca = Entry(ventana)
        e_marca.pack(pady=2)

        Label(ventana, text="Color:").pack()
        e_color = Entry(ventana)
        e_color.pack(pady=2)

        Label(ventana, text="Modelo:").pack()
        e_modelo = Entry(ventana)
        e_modelo.pack(pady=2)

        Label(ventana, text="Velocidad:").pack()
        e_vel = Entry(ventana)
        e_vel.pack(pady=2)

        Label(ventana, text="Caballaje:").pack()
        e_pot = Entry(ventana)
        e_pot.pack(pady=2)

        Label(ventana, text="Plazas:").pack()
        e_plazas = Entry(ventana)
        e_plazas.pack(pady=2)

        Label(ventana, text="Configuración de Ejes:").pack()
        e_eje = Entry(ventana)
        e_eje.pack()

        Label(ventana, text="Capacidad de Carga:").pack()
        e_cap = Entry(ventana)
        e_cap.pack()

        btnSave = Button(ventana, text="Guardar", command=lambda: "") 
        btnSave.pack(pady=5)
        Button(ventana, text="Volver", command=lambda: VistaGestion.cargar_submenu(ventana, tipo_actual)).pack(pady=5)

    @staticmethod
    def vista_listar_camiones(ventana):
        VistaGestion.limpiar_interfaz(ventana)
        Label(ventana).pack(pady=5)
        
        texto = ""
        registros=[
            ("1", "Volvo", "Blanco", "2022", "120", "540", "2", "3", "30 Ton"), 
            ("2", "Kenworth", "Negro", "2023", "110", "600", "2", "4", "45 Ton"),
            ("3", "Mercedes", "Plata", "2021", "130", "510", "2", "2", "25 Ton")] 
        if len(registros) > 0:
            idx = 1
            for r in registros:
                texto += f"\nCamión #{idx} | ID: {r[0]} \nMarca: {r[1]} | Color: {r[2]} | Modelo: {r[3]} | Velocidad: {r[4]} | Caballaje: {r[5]} | Plazas: {r[6]} | Ejes: {r[7]} | Capacidad: {r[8]}"
                idx += 1
        else:
            messagebox.showinfo(message="Sistema vacío.")

        Label(ventana, text=texto, justify=LEFT).pack(pady=5)
        Button(ventana, text="Regresar", command=lambda: VistaGestion.cargar_submenu(ventana, tipo_actual)).pack(pady=5)

    @staticmethod
    def vista_modificar_camiones(ventana):
        VistaGestion.limpiar_interfaz(ventana)
        Label(ventana).pack(pady=5)
        
        campos = ["ID", "Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas", "Ejes", "Capacidad"]
        entradas = []
        
        for c in campos:
            Label(ventana, text=f"{c}:").pack()
            e = Entry(ventana)
            e.pack()
            entradas.append(e)

        Button(ventana, text="Guardar Cambios", command=lambda: "").pack(pady=5)
        Button(ventana, text="Volver", command=lambda: VistaGestion.cargar_submenu(ventana, tipo_actual)).pack(pady=5)

    @staticmethod
    def vista_eliminar_camiones(ventana):
        VistaGestion.limpiar_interfaz(ventana)
        Label(ventana, text="Eliminar Registro de Camión").pack(pady=5)
        Label(ventana, text="ID a Eliminar:").pack()
        Entry(ventana).pack()
        Button(ventana, text="Eliminar", command=lambda: "").pack(pady=5)
        Button(ventana, text="Volver", command=lambda: VistaGestion.cargar_submenu(ventana, tipo_actual)).pack(pady=5)


    
    @staticmethod
    def vista_alta_camionetas(ventana):
        VistaGestion.limpiar_interfaz(ventana)
        Label(ventana).pack(pady=5)
        
        labels_text = ["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas"]
        entries = {}
        for l in labels_text:
            Label(ventana, text=f"{l}:").pack()
            e = Entry(ventana)
            e.pack(pady=2)
            entries[l] = e

        Label(ventana, text="Tipo de Tracción:").pack(pady=5)
        lst_traccion = Listbox(ventana, width=15, height=3, selectmode="single", exportselection=False)
        for op in ["Trasera", "Delantera", "4x4 Total"]:
            lst_traccion.insert(END, op)
        lst_traccion.pack()

        Label(ventana, text="¿Cabina Cerrada?:").pack(pady=5)
        lst_cerrada = Listbox(ventana, width=10, height=2, selectmode="single", exportselection=False)
        for op in ["Sí", "No"]:
            lst_cerrada.insert(END, op)
        lst_cerrada.pack()

        Button(ventana, text="Guardar Camioneta", command=lambda: "").pack(pady=10)
        Button(ventana, text="Cancelar", command=lambda: VistaGestion.cargar_submenu(ventana, tipo_actual)).pack(pady=5)

    @staticmethod
    def vista_listar_camionetas(ventana):
        VistaGestion.limpiar_interfaz(ventana)
        Label(ventana).pack(pady=5)
        
        texto = ""
        registros = "" 
        if len(registros) > 0:
            pass 
        else:
            messagebox.showinfo(message=f"No hay registros de {tipo_actual}.")

        Label(ventana, text=texto).pack(pady=5)
        Button(ventana, text="Regresar", command=lambda: VistaGestion.cargar_submenu(ventana, tipo_actual)).pack(pady=5)

    @staticmethod
    def vista_modificar_camionetas(ventana):
      
        VistaGestion.limpiar_interfaz(ventana)
        Label(ventana, text="Modificación de Camioneta").pack(pady=10)
        Button(ventana, text="Guardar", command=lambda: "").pack(pady=5)
        Button(ventana, text="Volver", command=lambda: VistaGestion.cargar_submenu(ventana, tipo_actual)).pack(pady=5)

    @staticmethod
    def vista_eliminar_camionetas(ventana):
        VistaGestion.limpiar_interfaz(ventana)
        Label(ventana).pack(pady=10)
        Label(ventana, text="ID:").pack()
        Entry(ventana).pack()
        Button(ventana, text="Borrar", command=lambda: "").pack(pady=5)
        Button(ventana, text="Volver", command=lambda: VistaGestion.cargar_submenu(ventana, tipo_actual)).pack(pady=5)


    
    @staticmethod
    def interfaz_busqueda_modificar(ventana):
        VistaGestion.limpiar_interfaz(ventana)
        
        Label(ventana).pack(pady=10)
        Label(ventana, text="Introduzca ID a buscar:").pack(pady=10)

        var_id = IntVar()
        entry_busqueda = Entry(ventana, textvariable=var_id)
        entry_busqueda.pack(pady=10)
        entry_busqueda.focus()
        
        if tipo_actual == "coches":
            btn = Button(ventana, text="Buscar Auto", 
                         command=lambda: controlador.Controladores.buscarId_modificar(ventana, var_id.get(), tipo_actual))
            btn.pack(pady=10)
        elif tipo_actual == "camiones":
            btn = Button(ventana, text="Buscar Camión", command=lambda: VistaGestion.vista_modificar_camiones(ventana))
            btn.pack(pady=10)
        elif tipo_actual == "camionetas":
            btn = Button(ventana, text="Buscar Camioneta", command=lambda: VistaGestion.vista_modificar_camionetas(ventana))
            btn.pack(pady=10)
            
        Button(ventana, text="Cancelar", command=lambda: VistaGestion.cargar_submenu(ventana, tipo_actual)).pack(pady=10)

    @staticmethod
    def interfaz_busqueda_eliminar(ventana):
        VistaGestion.limpiar_interfaz(ventana)
        
        Label(ventana).pack(pady=10)
        Label(ventana, text="Introduzca ID del vehículo:").pack(pady=10)

        var_id = IntVar()
        entry_busqueda = Entry(ventana, textvariable=var_id)
        entry_busqueda.pack(pady=10)
        entry_busqueda.focus()
        
        if tipo_actual == "coches":
            btn = Button(ventana, text="Borrar", 
                         command=lambda: controlador.Controladores.buscarId_eliminar(ventana, var_id.get(), tipo_actual))
            btn.pack(pady=10)
        elif tipo_actual == "camiones":
            btn = Button(ventana, text="Localizar", command=lambda: VistaGestion.vista_eliminar_camiones(ventana))
            btn.pack(pady=10)
        elif tipo_actual == "camionetas":
            btn = Button(ventana, text="Localizar", command=lambda: VistaGestion.vista_eliminar_camionetas(ventana))
            btn.pack(pady=10)

        Button(ventana, text="Cancelar", command=lambda: VistaGestion.cargar_submenu(ventana, tipo_actual)).pack(pady=10)