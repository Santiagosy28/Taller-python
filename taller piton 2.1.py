import tkinter as tk


lista_usuarios = [
    {"usuario": "1", "clave": "a", "rol": "admin"},
    {"usuario": "2", "clave": "b", "rol": "vendedor"},
    {"usuario": "3", "clave": "d", "rol": "usuario"},
]

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Inicio de sesión")
        self.master.geometry("300x200")
        self.setup_ui()

    def setup_ui(self):
        self.usuario_label = tk.Label(self.master, text="Usuario")
        self.usuario_label.pack()
        self.usuario_entry = tk.Entry(self.master)
        self.usuario_entry.pack(pady=5)

        self.clave_label = tk.Label(self.master, text="Contraseña")
        self.clave_label.pack()
        self.clave_entry = tk.Entry(self.master, show="*")
        self.clave_entry.pack(pady=5)

    
        self.mensaje_error = tk.Label(self.master, text="", fg="red")
        self.mensaje_error.pack(pady=5)

        self.login_button = tk.Button(self.master, text="Iniciar sesión", command=self.iniciar_sesion)
        self.login_button.pack(pady=20)

    def iniciar_sesion(self):
        try:
            usuario = self.usuario_entry.get().strip()  
            clave = self.clave_entry.get().strip()

            if not usuario or not clave:
                raise ValueError("Debe ingresar ambos campos.")

            
            usuario_valido = None
            for u in lista_usuarios:
                if u["usuario"] == usuario and u["clave"] == clave:
                    usuario_valido = u
                    break 

            if usuario_valido:
                self.mensaje_error.config(text="Inicio de sesión exitoso!", fg="green")
                self.mostrar_ventana(usuario_valido["rol"])
            else:
                raise ValueError("Usuario o clave incorrectos.")

        except ValueError as ve:
            self.mensaje_error.config(text=str(ve), fg="red")
        except Exception:
            self.mensaje_error.config(text="Ha ocurrido un error inesperado.", fg="red")

    def mostrar_ventana(self, rol):
        self.master.destroy()
        new_window = tk.Tk()
      
        colores = {"admin": "red", "vendedor": "green", "usuario": "blue"}
        color_fondo = colores.get(rol, "white")
        new_window.configure(bg=color_fondo)

        label = tk.Label(new_window, text=f"Bienvenido {rol}", font=("Arial", 20), bg=color_fondo, fg="white")
        label.pack(pady=20)

        logout_btn = tk.Button(new_window, text="Cerrar sesión", command=new_window.destroy)
        logout_btn.pack(pady=10)

        new_window.mainloop()
        
root = tk.Tk()
login_window = LoginWindow(root)
root.mainloop()
     