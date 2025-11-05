import tkinter as tk
from tkinter import ttk, messagebox

class Vista:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Vivero Vital")
        self.root.geometry("800x500")
        self.root.configure(bg="white")

        self.frame_login()

    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Información", mensaje)

   
    def frame_login(self):
        self.limpiar_pantalla()
        tk.Label(self.root, text="Iniciar Sesión", font=("Arial", 20), bg="lightyellow").pack(pady=30)
        self.user = tk.Entry(self.root)
        self.user.insert(0, "Admin")
        self.user.pack(pady=10)
        self.passw = tk.Entry(self.root, show="*")
        self.passw.pack(pady=10)
        tk.Button(self.root, text="Confirmar", bg="green", fg="white",
                  command=lambda: self.login_usuario()).pack(pady=20)

    def login_usuario(self):
        user = self.user.get()
        pw = self.passw.get()
        if self.controlador.verificar_usuario(user, pw):
            self.frame_menu()
        else:
            self.mostrar_mensaje("Usuario o contraseña incorrectos.")

    
    def frame_menu(self):
        self.limpiar_pantalla()
        tk.Label(self.root, text="Panel Principal - Vivero Vital", bg="lightgreen", font=("Arial", 16)).pack(fill="x")

        menu = tk.Frame(self.root, bg="white")
        menu.pack(pady=20)

        botones = [("Registrar Invernaderos", self.frame_registrar_invernadero),
                   ("Control Invernaderos", self.frame_listar_invernaderos),
                   ("Enfermedades", self.frame_enfermedades)]

        for texto, comando in botones:
            tk.Button(menu, text=texto, width=25, height=2, bg="lightyellow",
                      command=lambda c=comando: c()).pack(pady=5)

    
    def frame_registrar_invernadero(self):
        self.limpiar_pantalla()
        tk.Label(self.root, text="Registrar Invernadero", bg="lightgreen", font=("Arial", 16)).pack(fill="x")

        form = tk.Frame(self.root, bg="white")
        form.pack(pady=10)

        campos = ["Nombre", "Superficie (m²)", "Tipo cultivo", "Capacidad (toneladas)",
                  "Sistema riego", "Fecha creación", "Responsable"]
        self.entries = {}

        for campo in campos:
            tk.Label(form, text=campo, bg="white").pack()
            entrada = tk.Entry(form)
            entrada.pack(pady=3)
            self.entries[campo] = entrada

        tk.Label(form, text="", bg="lightblue", width=30, height=6).pack(pady=10)  

        tk.Button(form, text="Guardar", bg="green", fg="white",
                  command=lambda: self.guardar_invernadero()).pack(side="left", padx=20)
        tk.Button(form, text="Cancelar", bg="red", fg="white",
                  command=lambda: self.frame_menu()).pack(side="left", padx=20)

    def guardar_invernadero(self):
        datos = (
            self.entries["Nombre"].get(),
            self.entries["Superficie (m²)"].get(),
            self.entries["Tipo cultivo"].get(),
            self.entries["Capacidad (toneladas)"].get(),
            self.entries["Sistema riego"].get(),
            self.entries["Fecha creación"].get(),
            self.entries["Responsable"].get()
        )
        self.controlador.registrar_invernadero(datos)
        self.frame_menu()

  
    def frame_listar_invernaderos(self):
        self.limpiar_pantalla()
        tk.Label(self.root, text="Lista de Invernaderos", bg="lightgreen", font=("Arial", 16)).pack(fill="x")
        lista = tk.Frame(self.root)
        lista.pack(pady=10)

        datos = self.controlador.obtener_invernaderos()
        for inv in datos:
            tk.Label(lista, text=f"{inv[1]} - {inv[3]} ({inv[2]} m²)", bg="lightyellow").pack(pady=2)

        tk.Button(self.root, text="Volver", bg="red", fg="white",
                  command=lambda: self.frame_menu()).pack(pady=20)

  
    def frame_enfermedades(self):
        self.limpiar_pantalla()
        tk.Label(self.root, text="Registro de Enfermedades", bg="lightgreen", font=("Arial", 16)).pack(fill="x")

        form = tk.Frame(self.root, bg="white")
        form.pack(pady=20)

        etiquetas = ["Nombre", "Síntomas", "Tratamiento", "Cultivo afectado"]
        self.entry_enf = {}

        for campo in etiquetas:
            tk.Label(form, text=campo, bg="white").pack()
            e = tk.Entry(form)
            e.pack(pady=3)
            self.entry_enf[campo] = e

        tk.Label(form, text="", bg="lightblue", width=30, height=6).pack(pady=10)

        tk.Button(form, text="Guardar", bg="green", fg="white",
                  command=lambda: self.guardar_enfermedad()).pack(side="left", padx=20)
        tk.Button(form, text="Cancelar", bg="red", fg="white",
                  command=lambda: self.frame_menu()).pack(side="left", padx=20)

    def guardar_enfermedad(self):
        n = self.entry_enf["Nombre"].get()
        s = self.entry_enf["Síntomas"].get()
        t = self.entry_enf["Tratamiento"].get()
        c = self.entry_enf["Cultivo afectado"].get()
        self.controlador.registrar_enfermedad(n, s, t, c)
        self.frame_menu()
