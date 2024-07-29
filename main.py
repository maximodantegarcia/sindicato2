from tkinter import Tk
from ventana import Application

def main():
    ventana = Tk()
    ventana.wm_title("Base de datos Sindicato")
    ventana.config(bg='black')
    ventana.geometry("1920x1080")
    ventana.resizable(True, True)
    ventana.minsize(800, 600)
    
    app = Application(master=ventana)
    app.pack(fill="both", expand=True)
    
    ventana.mainloop()

if __name__ == "__main__":
    main()



