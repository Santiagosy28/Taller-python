import tkinter as tk
from vista import Vista
from controlador import Controlador

if __name__ == "__main__":
    root = tk.Tk()
    vista = Vista(root, None)
    controlador = Controlador(vista)
    vista.controlador = controlador
    root.mainloop()
