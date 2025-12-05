from model import cochesBD
from tkinter import messagebox

class Controladores():
    
    #SECCIÓN AUTOMÓVILES
    @staticmethod
    def insertar_coche(marca, color, modelo, velocidad, potencia, plazas):
        respuesta = cochesBD.Autos.insertar(marca, color, modelo, velocidad, potencia, plazas)
        if respuesta:
            messagebox.showinfo(message="La acción se ha realizado exitosamente", title="Agregar nuevo coche")
        else:
            messagebox.showinfo(message="No se ha podido realizar la acción", title="Error", icon="warning")

    @staticmethod
    def mostrar_coche():
        registros = cochesBD.Autos.consultar()
        if len(registros) > 0:
            return registros
        else:
            messagebox.showinfo(message="No existe ningun registro por el momento", title="No hay registros", icon="warning")
            return []

    @staticmethod
    def actualizar_coche(marca, color, modelo, velocidad, potencia, plazas, id):
        respuesta = cochesBD.Autos.actualizar(marca, color, modelo, velocidad, potencia, plazas, id)
        if respuesta:
            messagebox.showinfo(message=f"Se ha cambiado el coche de id: {id} exitosamente", title="Modificar coche")
        else:
            messagebox.showinfo(message="No se ha podido realizar la acción", title="Error", icon="warning")
    
    @staticmethod
    def eliminar_coche(id):
        respuesta = cochesBD.Autos.eliminar(id)
        if respuesta:
            messagebox.showinfo(message=f"Se ha eliminado el coche de id: {id} exitosamente", title="Eliminar coche")
        else:
            messagebox.showinfo(message="No se ha podido realizar la acción", title="Error", icon="warning")


    # SECCIÓN CAMIONES 
    @staticmethod
    def insertar_camion(marca, color, modelo, velocidad, potencia, plazas, ejes, capacidad):
        respuesta = cochesBD.Camiones.insertar(marca, color, modelo, velocidad, potencia, plazas, ejes, capacidad)
        if respuesta:
            messagebox.showinfo(message="Camión registrado exitosamente", title="Agregar Camión")
        else:
            messagebox.showinfo(message="Error al guardar el camión", title="Error", icon="warning")

    @staticmethod
    def mostrar_camion():
        registros = cochesBD.Camiones.consultar()
        if len(registros) > 0:
            return registros
        else:
            messagebox.showinfo(message="No hay camiones registrados", title="Sin registros", icon="info")
            return []

    @staticmethod
    def actualizar_camion(marca, color, modelo, velocidad, potencia, plazas, ejes, capacidad, id):
        respuesta = cochesBD.Camiones.actualizar(marca, color, modelo, velocidad, potencia, plazas, ejes, capacidad, id)
        if respuesta:
            messagebox.showinfo(message=f"Camión ID {id} actualizado exitosamente", title="Modificar Camión")
        else:
            messagebox.showinfo(message="Error al actualizar el camión", title="Error", icon="warning")

    @staticmethod
    def eliminar_camion(id):
        respuesta = cochesBD.Camiones.eliminar(id)
        if respuesta:
            messagebox.showinfo(message=f"Camión ID {id} eliminado", title="Eliminar Camión")
        else:
            messagebox.showinfo(message="Error al eliminar el camión", title="Error", icon="warning")


    # SECCIÓN CAMIONETAS 
    def insertar_camioneta(marca, color, modelo, velocidad, potencia, plazas, traccion, cerrada):
        respuesta = cochesBD.Camionetas.insertar(marca, color, modelo, velocidad, potencia, plazas, traccion, cerrada)
        if respuesta:
            messagebox.showinfo(message="Camioneta registrada exitosamente", title="Agregar Camioneta")
        else:
            messagebox.showinfo(message="Error al guardar la camioneta", title="Error", icon="warning")

    @staticmethod
    def mostrar_camioneta():
        registros = cochesBD.Camionetas.consultar()
        if len(registros) > 0:
            return registros
        else:
            messagebox.showinfo(message="No hay camionetas registradas", title="Sin registros", icon="info")
            return []

    @staticmethod
    def actualizar_camioneta(marca, color, modelo, velocidad, potencia, plazas, traccion, cerrada, id):
        respuesta = cochesBD.Camionetas.actualizar(marca, color, modelo, velocidad, potencia, plazas, traccion, cerrada, id)
        if respuesta:
            messagebox.showinfo(message=f"Camioneta ID {id} actualizada exitosamente", title="Modificar Camioneta")
        else:
            messagebox.showinfo(message="Error al actualizar la camioneta", title="Error", icon="warning")

    @staticmethod
    def eliminar_camioneta(id):
        respuesta = cochesBD.Camionetas.eliminar(id)
        if respuesta:
            messagebox.showinfo(message=f"Camioneta ID {id} eliminada", title="Eliminar Camioneta")
        else:
            messagebox.showinfo(message="Error al eliminar la camioneta", title="Error", icon="warning")


    # BUSCADORES GENerales
    @staticmethod
    def buscarId_eliminar(ventana, opid, tipo):
        from view.vista import VistaGestion 
       
        registros = []
        if tipo == "coches":
            registros = cochesBD.Autos.consultar()
        elif tipo == "camiones":
            registros = cochesBD.Camiones.consultar()
        elif tipo == "camionetas":
            registros = cochesBD.Camionetas.consultar()
            
        encontrado = False 
        
        for filas in registros:
           
            if str(filas[0]) == str(opid):
                encontrado = True
                if tipo == "coches":
                    VistaGestion.vista_eliminar_coche(ventana, opid)
                elif tipo == "camionetas":
                  
                    VistaGestion.vista_eliminar_camionetas(ventana) 
                elif tipo == "camiones":
                    VistaGestion.vista_eliminar_camiones(ventana)
                return
        
        if not encontrado:
            messagebox.showinfo(message=f"No se encontró el ID {opid} en {tipo}", title="ID no encontrado")

    @staticmethod
    def buscarId_modificar(ventana, opid, tipo):
        from view.vista import VistaGestion
        
        registros = []
        if tipo == "coches":
            registros = cochesBD.Autos.consultar()
        elif tipo == "camiones":
            registros = cochesBD.Camiones.consultar()
        elif tipo == "camionetas":
            registros = cochesBD.Camionetas.consultar()

        encontrado = False
        
        for filas in registros:
            if str(filas[0]) == str(opid):
                encontrado = True
                if tipo == "coches":
                    VistaGestion.vista_modificar_coche(ventana, filas)
                elif tipo == "camionetas":
                    VistaGestion.vista_modificar_camionetas(ventana, filas)
                elif tipo == "camiones":
                    VistaGestion.vista_modificar_camiones(ventana, filas)
                return
        
        if not encontrado:
            messagebox.showwarning(message=f"No se encontró el ID {opid} en {tipo}", title="No encontrado")