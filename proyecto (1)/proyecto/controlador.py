from modelo import Modelo

class Controlador:
    def __init__(self, vista):
        self.modelo = Modelo()
        self.vista = vista
        self.enfermedades_temp = {}  

   
    def verificar_usuario(self, usuario, contrasena):
        usuarios = [("Admin", "12345"), ("Maria", "abc123")]
        return (usuario, contrasena) in usuarios


    def registrar_invernadero(self, datos):
        self.modelo.insertar_invernadero(datos)
        self.vista.mostrar_mensaje("Invernadero registrado correctamente.")

    
    def registrar_enfermedad(self, nombre, sintomas, tratamiento, cultivo):
        self.enfermedades_temp[nombre] = {
            "sintomas": sintomas,
            "tratamiento": tratamiento,
            "cultivo_afectado": cultivo
        }
   
        self.modelo.insertar_enfermedad((nombre, sintomas, tratamiento, cultivo))
        self.vista.mostrar_mensaje("Enfermedad registrada y guardada en la base de datos.")

    
    def obtener_invernaderos(self):
        return self.modelo.obtener_invernaderos()
