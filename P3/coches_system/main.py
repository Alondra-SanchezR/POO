from tkinter import *
from view import vista
class App():
    def __init__(self,ventana):
        vista.Menu(ventana)

if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()