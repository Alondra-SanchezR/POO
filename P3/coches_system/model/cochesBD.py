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