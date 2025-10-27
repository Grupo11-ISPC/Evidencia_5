import mysql.connector
from mysql.connector import Error

class ConexionDB:
    # Datos de conexión
    _HOST = 'localhost'
    _PORT = 3306
    _DATABASE = 'smart_home_solutions'
    _USER = 'root'
    _PASSWORD = 'admin'
    
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
                    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
                    nombre VARCHAR(100),
                    email VARCHAR(100) UNIQUE,
                    password VARCHAR(255),
                    rol ENUM('admin', 'user') DEFAULT 'user'
                )
            """)
            
            # Tabla dispositivos
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS dispositivos (
                    id_dispositivo INT PRIMARY KEY AUTO_INCREMENT,
                    nombre_dispositivo VARCHAR(100),
                    tipo_dispositivo VARCHAR(50),
                    estado_dispositivo TINYINT DEFAULT 0,
                    id_usuario INT,
                    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
                )
            """)
            
            # Tabla automatizaciones
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS automatizaciones (
                    id_automatizacion INT PRIMARY KEY AUTO_INCREMENT,
                    descripcion VARCHAR(255),
                    condicion VARCHAR(255),
                    id_usuario INT,
                    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
                )
            """)
            
            # Tabla acciones
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS acciones (
                    id_accion INT PRIMARY KEY AUTO_INCREMENT,
                    tipo_accion VARCHAR(50),
                    valor_configurado VARCHAR(255),
                    id_automatizacion INT,
                    id_dispositivo INT,
                    FOREIGN KEY (id_automatizacion) REFERENCES automatizaciones(id_automatizacion) ON DELETE CASCADE,
                    FOREIGN KEY (id_dispositivo) REFERENCES dispositivos(id_dispositivo) ON DELETE CASCADE
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