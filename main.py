from tkinter import *
from ventana import *

def main():
    ventana = Tk()
    ventana.wm_title("Base de datos Sindicato")
    ventana.config(bg='black')
    ventana.geometry('1920x1080')
    ventana.resizable(False)
    ventana()
    app = Registro(ventana)
    app.mainloop()

    
if __name__ == "__main__":
    ventana = Tk()
    app = Registro(ventana)
    ventana.mainloop()
    
