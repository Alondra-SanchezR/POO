from tkinter import *
from view.vista import VistaGestion

class App():
    def __init__(self,ventana):
        VistaGestion(ventana)

if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()