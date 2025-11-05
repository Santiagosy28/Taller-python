import pymysql

class Modelo:
    def __init__(self):
        self.conexion = pymysql.connect(
            host="localhost",
            user="root",             
            password="",             
            database="vivero_vital"  
        )
        self.cursor = self.conexion.cursor()
        print(" Conectado a la base de datos vivero_vital")

    def insertar_invernadero(self, datos):
        sql = """
        INSERT INTO invernaderos 
        (nombre, superficie, tipo_cultivo, capacidad, sistema_riego, fecha_creacion, responsable)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(sql, datos)
        self.conexion.commit()

    def insertar_enfermedad(self, datos):
        sql = """
        INSERT INTO enfermedades (nombre, sintomas, tratamiento, cultivo_afectado)
        VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(sql, datos)
        self.conexion.commit()

    def obtener_invernaderos(self):
        self.cursor.execute("SELECT * FROM invernaderos")
        return self.cursor.fetchall()
