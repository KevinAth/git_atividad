import tkinter as tk

class ventanaM(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ventana")
        self.geometry("300x300")
        etiqueta = tk.Label(self,text="Hola mundo")
        etiqueta.pack()
        entrada = tk.Entry(self)
        entrada.pack()
        
        boton = tk.Button(self, text="confirmar")
        boton.pack()
        segEtiqueta = tk.Label(self,text="Fin")
        segEtiqueta.pack()
        
        
