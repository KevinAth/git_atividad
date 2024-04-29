import tkinter as tk

class ventanaM(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ventana")
        self.geometry("300x300")
        etiqueta = tk.Label(self,text="Hola mundo")
        etiqueta.pack()
        
