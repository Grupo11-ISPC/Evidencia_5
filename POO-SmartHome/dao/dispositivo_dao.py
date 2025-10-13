from .interfaces.i_dispositivo_dao import IDispositivoDAO
from conn.db_conn import conn, cursor
from dominio.dispositivo import Dispositivo
import sqlite3

class DispositivoDAO(IDispositivoDAO):
    def guardar(self, dispositivo):
        try:
            estado_int = 1 if dispositivo.get_estado() == "Encendido" else 0
            cursor.execute(
                "INSERT INTO dispositivos (nombre, tipo, estado) VALUES (?, ?, ?)",
                (dispositivo.get_nombre_dispositivo(), dispositivo.get_tipo(), estado_int))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error al guardar dispositivo: {e}")
            conn.rollback()
            return None
        

    def listar(self):
        try:
            cursor.execute("SELECT * FROM dispositivos")
            return cursor.fetchall()  # devuelve lista de tuplas: (id, nombre, tipo, estado, usuario_id)
        except sqlite3.Error as e:
            print(f"Error al listar dispositivos: {e}")
            return []

    def modificar(self, dispositivo: Dispositivo):
        try:
            if dispositivo.get_id() is None:
                raise ValueError("Dispositivo debe tener un ID para modificarlo")
            
            estado_int = 1 if dispositivo.get_estado() == "Encendido" else 0
            cursor.execute(
                "UPDATE dispositivos SET nombre = ?, tipo = ?, estado = ? WHERE id = ?",
                (dispositivo.get_nombre_dispositivo(), dispositivo.get_tipo(), estado_int, dispositivo.get_id())
        )
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error al modificar dispositivo: {e}")
            conn.rollback()

    def eliminar(self, dispositivo):
        try:
            if dispositivo.get_id() is None:
                raise ValueError("Dispositivo debe tener un ID para eliminarlo")
            cursor.execute("DELETE FROM dispositivos WHERE id = ?", (dispositivo.get_id(),))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error al eliminar dispositivo: {e}")
            conn.rollback()

    def obtener_por_id(self, id):
        try:
            cursor.execute("SELECT * FROM dispositivos WHERE id = ?", (id,))
            fila = cursor.fetchone()
            if fila:
                return Dispositivo(fila[1], fila[2], bool(fila[3]), id=fila[0])
            return None
        except sqlite3.Error as e:
            print(f"Error al obtener dispositivo por ID: {e}")
            return None

