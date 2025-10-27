import mysql.connector
from mysql.connector import Error

class ConexionDB:
    # Datos de conexión
    _HOST = 'localhost'
    _PORT = 3306
    _DATABASE = 'smart_home_solutions'
    _USER = 'root'
    _PASSWORD = ''
    
    @staticmethod
    def get_conexion():

        try:
            conexion = mysql.connector.connect(
                host=ConexionDB._HOST,
                port=ConexionDB._PORT,
                database=ConexionDB._DATABASE,
                user=ConexionDB._USER,
                password=ConexionDB._PASSWORD
            )
            
            if conexion.is_connected():
                return conexion
            
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            return None
    
    @staticmethod
    def cerrar_conexion(conexion):
        """Cierra la conexión a la base de datos"""
        if conexion and conexion.is_connected():
            conexion.close()
    
    @staticmethod
    def inicializar_bd():
        """Crea las tablas si no existen"""
        conexion = None
        try:
            conexion = mysql.connector.connect(
                host=ConexionDB._HOST,
                port=ConexionDB._PORT,
                user=ConexionDB._USER,
                password=ConexionDB._PASSWORD
            )
            
            cursor = conexion.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {ConexionDB._DATABASE}")
            cursor.execute(f"USE {ConexionDB._DATABASE}")
            
            # Tabla usuarios
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    rol ENUM('admin', 'user') NOT NULL,
                    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Tabla dispositivos
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS dispositivos (
                    id_dispositivo INT AUTO_INCREMENT PRIMARY KEY,
                    nombre_dispositivo VARCHAR(100) NOT NULL,
                    tipo_dispositivo VARCHAR(50) NOT NULL,
                    estado_dispositivo BOOLEAN DEFAULT FALSE,
                    id_usuario INT NOT NULL,
                    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE
                )
            """)
            
            # Tabla automatizaciones
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS automatizaciones (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    descripcion VARCHAR(255) NOT NULL,
                    condicion TEXT,
                    id_usuario INT NOT NULL,
                    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE
                )
            """)
            
            # Tabla acciones
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS acciones (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    tipo_accion VARCHAR(50) NOT NULL,
                    valor_configurado VARCHAR(255),
                    id_automatizacion INT NOT NULL,
                    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (id_automatizacion) REFERENCES automatizaciones(id) ON DELETE CASCADE
                )
            """)
            
            conexion.commit()
            print("Base de datos y tablas creadas/verificadas correctamente")
            
        except Error as e:
            print(f"Error al inicializar la base de datos: {e}")
            
        finally:
            if conexion and conexion.is_connected():
                cursor.close()
                conexion.close()