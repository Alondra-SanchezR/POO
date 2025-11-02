from tkinter import *

ventana=Tk()
ventana.geometry("600x400")
ventana.title("Uso del Main Loop")

marco1=Frame(ventana,width=600,height=50,bg="#e80606",border=2,relief="raised").pack()
marco2=Frame(ventana,width=600,height=50,bg="#e86406",border=2,relief="raised").pack()
marco3=Frame(ventana,width=600,height=50,bg="#e1e806",border=2,relief="raised").pack()
marco4=Frame(ventana,width=600,height=50,bg="#24e806",border=2,relief="raised").pack()
marco5=Frame(ventana,width=600,height=50,bg="#1a4fee",border=2,relief="raised").pack()
marco6=Frame(ventana,width=600,height=50,bg="#8f1aee",border=2,relief="raised").pack()

ventana.mainloop()
