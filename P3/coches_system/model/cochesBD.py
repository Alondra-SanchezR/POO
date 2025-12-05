from conexionBD import *

class Autos: 
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas):
        try:
            sql = "INSERT INTO autos VALUES(null, %s, %s, %s, %s, %s, %s)"
            valores = (marca, color, modelo, velocidad, caballaje, plazas)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except:
            return False
       
    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM autos")
            return cursor.fetchall()
        except:    
            return []

    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, id):
        try:
            sql = "UPDATE autos SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s WHERE id=%s"
            valores = (marca, color, modelo, velocidad, caballaje, plazas, id)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except: 
            return False

    @staticmethod
    def eliminar(id):
        try:
            sql = "DELETE FROM autos WHERE id=%s"
            cursor.execute(sql, (id,))
            conexion.commit() 
            return True  
        except:    
            return False

class Camiones:
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, ejes, capacidad):
        try:
            sql = "INSERT INTO camiones VALUES(null, %s, %s, %s, %s, %s, %s, %s, %s)"
            valores = (marca, color, modelo, velocidad, caballaje, plazas, ejes, capacidad)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except:
            return False
       
    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM camiones")
            return cursor.fetchall()
        except:    
            return []

    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, ejes, capacidad, id):
        try:
            sql = "UPDATE camiones SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, ejes=%s, capacidad=%s WHERE id=%s"
            valores = (marca, color, modelo, velocidad, caballaje, plazas, ejes, capacidad, id)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except: 
            return False

    @staticmethod
    def eliminar(id):
        try:
            sql = "DELETE FROM camiones WHERE id=%s"
            cursor.execute(sql, (id,))
            conexion.commit() 
            return True  
        except:    
            return False

class Camionetas:
    @staticmethod
    def insertar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        try:
            sql = "INSERT INTO camionetas VALUES(null, %s, %s, %s, %s, %s, %s, %s, %s)"
            valores = (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except:
            return False
       
    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM camionetas")
            return cursor.fetchall()
        except:    
            return []

    @staticmethod
    def actualizar(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id):
        try:
            sql = "UPDATE camionetas SET marca=%s, color=%s, modelo=%s, velocidad=%s, caballaje=%s, plazas=%s, traccion=%s, cerrada=%s WHERE id=%s"
            valores = (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada, id)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except: 
            return False

    @staticmethod
    def eliminar(id):
        try:
            sql = "DELETE FROM camionetas WHERE id=%s"
            cursor.execute(sql, (id,))
            conexion.commit() 
            return True  
        except:    
            return False