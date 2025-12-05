from model import cochesBD
from tkinter import messagebox

class Controladores():
    @staticmethod
    def insertar_coche(marca, color, modelo, velocidad, potencia, plazas):
        respuesta = cochesBD.Autos.insertar(marca, color, modelo, velocidad, potencia, plazas)
        if respuesta:
            messagebox.showinfo(message="La acción se ha realizado exitosamente", title="Agregar nuevo coche")
        else:
            messagebox.showinfo(message="No se ha podido realizar la acción", title="Ha ocurrido un error, intente de nuevo", icon="warning")

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
            messagebox.showinfo(message="No se ha podido realizar la acción", title="Ha ocurrido un error, intente de nuevo", icon="warning")
    
    @staticmethod
    def eliminar_coche(id):
        respuesta = cochesBD.Autos.eliminar(id)
        if respuesta:
            messagebox.showinfo(message=f"Se ha eliminado el coche de id: {id} exitosamente", title="Eliminar coche")
        else:
            messagebox.showinfo(message="No se ha podido realizar la acción", title="Ha ocurrido un error, intente de nuevo", icon="warning")

    @staticmethod
    def buscarId_eliminar(ventana, opid, tipo):
        from view.vista import VistaGestion 
        
        registro = cochesBD.Autos.consultar()
        encontrado = False 
        
        for filas in registro:
            if filas[0] == opid:
                encontrado = True
                if tipo == "coches":
                    VistaGestion.vista_eliminar_coche(ventana, opid)
                elif tipo == "camionetas":
                    VistaGestion.vista_eliminar_camionetas(ventana)
                elif tipo == "camiones":
                    VistaGestion.vista_eliminar_camiones(ventana)
                return
        
        if not encontrado:
            messagebox.showinfo(message="No se encontro el", title="Ocurrio un problema")

    @staticmethod
    def buscarId_modificar(ventana, opid, tipo):
        from view.vista import VistaGestion
        
        registro = cochesBD.Autos.consultar()
        encontrado = False
        
        for filas in registro:
            if filas[0] == opid:
                encontrado = True
                if tipo == "coches":
                    VistaGestion.vista_modificar_coche(ventana, opid)
                elif tipo == "camionetas":
                    VistaGestion.vista_modificar_camionetas(ventana)
                elif tipo == "camiones":
                    VistaGestion.vista_modificar_camiones(ventana)
                return
        
        if not encontrado:
            messagebox.showinfo(message="No se encontro el id", title="Ocurrio un problema")