import os
os.system("clear")
from model import cochesBD
from tkinter import messagebox

class Coches:
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
       self._marca=marca
       self._color=color
       self._modelo=modelo
       self._velocidad=velocidad
       self._caballaje=caballaje
       self._plazas=plazas
 
    @property
    def marca(self):
       return self._marca
    
    @marca.setter
    def marca(self,marca):
       self._marca=marca
    
    @property
    def color(self):
       return self._color
    
    @color.setter
    def color(self,color):
       self._color=color 

    @property
    def modelo(self):
       return self._modelo

    @modelo.setter
    def modelo(self,modelo):
       self._modelo=modelo

    @property
    def velocidad(self):
       return self._velocidad

    @velocidad.setter
    def velocidad(self,velocidad):
       self._velocidad=velocidad 

    @property
    def caballaje(self):
       return self._caballaje

    @caballaje.setter
    def caballaje(self,caballaje):
       self._caballaje=caballaje

    @property
    def plazas(self):
       return self._plazas

    @plazas.setter
    def plazas(self,plazas):
       self._plazas=plazas                   

    def acelerar(self):
      return "Estas acelerando el coche"

    def frenar(self):
      return "Estas frenando el coche"  


class Camiones(Coches):
   def __init__(self,marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga):
      super().__init__(marca,color,modelo,velocidad,caballaje,plazas)
      self.__eje=eje
      self.__capacidadCarga=capacidadCarga
   
   def cargar(self,tipo_carga):
      self.tipo_carga=tipo_carga
      return self.tipo_carga
   
   def acelerar(self):
       return "Estas acelerando el camion"
   
   def frenar(self):
       return "Estas frenando el camion" 

   @property
   def eje(self):
      return self.__eje
   
   @eje.setter
   def eje(self,eje):
      self.__eje=eje
   
   @property
   def capacidadCarga(self):
      return self.__capacidadCarga
   
   @capacidadCarga.setter
   def capacidadCarga(self,capacidadCarga):
      self.__capacidadCarga=capacidadCarga
      
   
class Camionetas(Coches):
   def __init__(self,marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada):
      super().__init__(marca,color,modelo,velocidad,caballaje,plazas)
      self.__traccion=traccion
      self.__cerrada=cerrada
   
   def transportar(self,num_pasajeros):
      self.num_pasajeros=num_pasajeros
      return self.num_pasajeros
   
   def acelerar(self):
      return "Estas acelerando la camioneta"
   
   def frenar(self):
      return "Estas frenando la camioneta" 

   @property
   def traccion(self):
      return self.__traccion
   
   @traccion.setter
   def eje(self,traccion):
      self.__traccion=traccion
   
   @property
   def cerrada(self):
      return self.__cerrada
   
   @cerrada.setter
   def cerrada(self,cerrada):
      self.__cerrada=cerrada
   
class funciones():
   @staticmethod
   def respuesta_sql(respuesta):
      if respuesta:
            result=messagebox.showinfo(title="Status", message="Se realizó la acción exitosamente")
      else:
            result=messagebox.showerror(title="Status", message="No se pudo realizar la acción, inténtelo más tarde")


   @staticmethod
   def insertar_vehiculo(tipo,nombre,color,modelo,velocidad,potencia,plaza,extra1,extra2):
      if tipo=="autos":
         resp=cochesBD.Autos.insertar(nombre,color,modelo,velocidad,potencia,plaza)
      elif tipo=="camionetas":
         resp=cochesBD.Camionetas.insertar(nombre,color,modelo,velocidad,potencia,plaza,extra1,extra2)
      elif tipo=="camiones":
         resp=cochesBD.Camiones.insertar(nombre,color,modelo,velocidad,potencia,plaza,extra1,extra2)
      if resp:
         funciones.respuesta_sql(resp)
         return resp

   def imprimir_datos_vehiculo(self,marca,color,modelo,velocidad,potencia,plazas):
      print(f"\n\tDatos del Vehiculo: \n Marca:{marca} \n Color: {color} \n Modelo: {modelo} \n Velocidad: {velocidad} \n Caballaje: {potencia} \n Plazas: {plazas}")


   def autos(self):
      marca,color,modelo,velocidad,potencia,plazas=self.datos_autos("Auto")
      coche=coche.Coches(marca,color,modelo,velocidad,potencia,plazas)
      self.borrarPantalla()
      self.imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
      return coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas
      
   def camionetas(self):
      marca,color,modelo,velocidad,potencia,plazas=self.datos_autos("Camioneta")
      traccion=input("Traccion: ").upper().strip()
      cerrada=input("Cerrada (SI/NO): ").upper().strip()
      if cerrada=="SI":
            cerrada=True
      else:
            cerrada=False    
      coche=coche.Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
      self.borrarPantalla()
      self.imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
      print(f" Traccion: {coche.traccion}\n Cerrada: {coche.cerrada}")
      return coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas,coche.traccion,coche.cerrada 

   def camiones(self):
      marca,color,modelo,velocidad,potencia,plazas=self.datos_autos("Camión")
      eje=int(input("No.de ejes: "))
      capacidadCarga=int(input("Capacidad de carga: "))
      coche=coche.Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
      self.borrarPantalla()
      self.imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
      print(f"#Ejes: {coche.eje}\n Capacidad de carga: {coche.capacidadCarga}")
      return coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas,coche.eje,coche.capacidadCarga

      def menu_autos(self, ventana):
         while True:
            self.borrarPantalla(ventana)
            opcion=self.menu_acciones("Autos")
            if opcion == '1' or opcion=="INSERTAR":
                  self.borrarPantalla(ventana)
                  marca,color,modelo,velocidad,caballaje,plazas=self.autos()
                  #Agregar a BD
                  auto=cochesBD.Autos(marca,color,modelo,velocidad,caballaje,plazas)
                  respuesta=auto.insertar()
                  self.respuesta_sql(respuesta) 
                  self.esperarTecla()    
            elif opcion == '2' or opcion=="CONSULTAR":
                  self.borrarPantalla(ventana)  
                  registros=cochesBD.Autos.consultar()
                  if len(registros)>0:
                     num_autos=1
                     for fila in registros:
                        print(f"\nAuto #{num_autos} con ID: {fila[0]} \nMarca: {fila[1]} \nColor: {fila[2]} Modelo: {fila[3]} \nVelocidad: {fila[4]} \nPotencia: {fila[5]}\nPlazas: {fila[6]}") 
                        num_autos+=1    
                     self.esperarTecla()
                  else:
                     print(f"\n \t \t... ¡ No existen datos que mostrar, por el momento ! ...")
                     self.esperarTecla()            
            elif opcion == '3' or opcion=="ACTUALIZAR":
                  self.borrarPantalla(ventana)
                  print(f"\n \t .:: Actualizar Auto ::. \n")
                  id=input("\nID: ")
                  marca,color,modelo,velocidad,caballaje,plazas=self.autos() 
                  respuesta=cochesBD.Autos.actualizar(marca,color,modelo,velocidad,caballaje,plazas,id)
                  self.respuesta_sql(respuesta)  
                  self.esperarTecla()      
            elif opcion == '4' or opcion=="ELIMINAR":
                  self.borrarPantalla(ventana)
                  print(f"\n \t .:: Eliminar Auto ::. \n")
                  id=input("\nID: ")
                  respuesta=cochesBD.Autos.eliminar(id)
                  self.respuesta_sql(respuesta)  
                  self.esperarTecla()    
            elif opcion == '5' or opcion=="SALIR":
                  break
            else:
                  print("\n \t \t Opción no válida. Intenta de nuevo.")
                  self.esperarTecla()

      def menu_camionetas(self, ventana):
         while True:
            self.borrarPantalla(ventana)
            opcion=self.menu_acciones("Camionetas")
            if opcion == '1' or opcion=="INSERTAR":
                  self.borrarPantalla(ventana)
                  marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada=self.camionetas()
                  respuesta=cochesBD.Camionetas.insertar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
                  self.respuesta_sql(respuesta) 
                  self.esperarTecla()    
            elif opcion == '2' or opcion=="CONSULTAR":
                  self.borrarPantalla(ventana)  
                  registros=cochesBD.Camionetas.consultar()
                  if len(registros)>0:
                     num_autos=1
                     for fila in registros:
                        print(f"\nCamioneta #{num_autos} con ID: {fila[0]} \nMarca: {fila[1]} \nColor: {fila[2]} Modelo: {fila[3]} \nVelocidad: {fila[4]} \nPotencia: {fila[5]}\nPlazas: {fila[6]}\nTracción: {fila[7]}\nCerrada: {fila[8]}") 
                        num_autos+=1    
                     self.esperarTecla()
                  else:
                     print(f"\n \t \t... ¡ No existen datos que mostrar, por el momento ! ...")
                     self.esperarTecla()            
            elif opcion == '3' or opcion=="ACTUALIZAR":
                  self.borrarPantalla(ventana)
                  print(f"\n \t .:: Actualizar Camioneta ::. \n")
                  id=input("\nID: ")
                  marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada=self.camionetas()
                  respuesta=cochesBD.Camionetas.actualizar(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada,id)
                  self.respuesta_sql(respuesta)
                  self.esperarTecla()      
            elif opcion == '4' or opcion=="ELIMINAR":
                  self.borrarPantalla(ventana)
                  print(f"\n \t .:: Eliminar Camioneta ::. \n")
                  id=input("\nID: ")
                  respuesta=cochesBD.Camionetas.eliminar(id)
                  self.respuesta_sql(respuesta) 
                  self.esperarTecla()    
            elif opcion == '5' or opcion=="SALIR":
                  break
            else:
                  print("\n \t \t Opción no válida. Intenta de nuevo.")
                  self.esperarTecla()

      def menu_camiones(self, ventana):
         while True:
            self.borrarPantalla(ventana)
            opcion=self.menu_acciones("Camiones")
            if opcion == '1' or opcion=="INSERTAR":
                  self.borrarPantalla(ventana)
                  marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga=self.camiones()
                  respuesta=cochesBD.Camiones.insertar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga)
                  self.respuesta_sql(respuesta)
                  self.esperarTecla()    
            elif opcion == '2' or opcion=="CONSULTAR":
                  self.borrarPantalla(ventana)  
                  registros=cochesBD.Camiones.consultar()
                  if len(registros)>0:
                     num_autos=1
                     for fila in registros:
                        print(f"\nCamion # {num_autos} con ID: {fila[0]} \nMarca: {fila[1]} \nColor: {fila[2]} Modelo: {fila[3]} \nVelocidad: {fila[4]} \nPotencia: {fila[5]}\nPlazas: {fila[6]}\nNo. ejes: {fila[7]}\nCapacidad de Carga: {fila[8]}") 
                        num_autos+=1    
                     self.esperarTecla()
                  else:
                     print(f"\n \t \t... ¡ No existen datos que mostrar, por el momento ! ...")
                     self.esperarTecla()            
            elif opcion == '3' or opcion=="ACTUALIZAR":
                  self.borrarPantalla(ventana)
                  print(f"\n \t .:: Actualizar Camion ::. \n")
                  id=input("\nID: ")
                  marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga=self.camiones()
                  #Actualizar BD
                  respuesta=cochesBD.Camiones.actualizar(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id)
                  self.respuesta_sql(respuesta)
                  self.esperarTecla()      
            elif opcion == '4' or opcion=="ELIMINAR":
                  self.borrarPantalla(ventana)
                  print(f"\n \t .:: Eliminar Camion ::. \n")
                  id=input("\nID: ")
                  respuesta=cochesBD.Camiones.eliminar(id)
                  self.respuesta_sql(respuesta)  
                  self.esperarTecla()    
            elif opcion == '5' or opcion=="SALIR":
                  break
            else:
                  print("\n \t \t Opción no válida. Intenta de nuevo.")
                  self.esperarTecla()