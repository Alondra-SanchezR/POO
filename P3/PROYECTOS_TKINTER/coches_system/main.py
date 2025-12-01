import tkinter as tk
from view import vista

class App():
    def __init__(self, ventana):
        app=vista.Menu(ventana)

if __name__ == "__main__":
    ventana=tk.Tk()
    app=App(ventana)
    ventana=tk.mainloop()