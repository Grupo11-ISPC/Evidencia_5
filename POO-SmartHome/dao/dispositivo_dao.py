from .interfaces.i_dispositivo_dao import IDispositivoDAO
from conn.db_conn import conn, cursor
from dominio.dispositivo import Dispositivo

class DispositivoDAO(IDispositivoDAO):
    def guardar(self, dispositivo):
        estado_int = 1 if dispositivo.get_estado() == "Encendido" else 0
        cursor.execute(
            "INSERT INTO dispositivos (nombre, tipo, estado) VALUES (?, ?, ?)",
            (dispositivo.get_nombre_dispositivo(), dispositivo.get_tipo(), estado_int))
    
        conn.commit()

    def listar(self):
        cursor.execute("SELECT * FROM dispositivos")
        return cursor.fetchall()  # devuelve lista de tuplas: (id, nombre, tipo, estado, usuario_id)

    def modificar(self, dispositivo: Dispositivo):
        estado_int = 1 if dispositivo.get_estado() == "Encendido" else 0
        if dispositivo.get_id() is None:
            raise ValueError("Dispositivo debe tener un ID para modificarlo")
        cursor.execute(
            "UPDATE dispositivos SET nombre = ?, tipo = ?, estado = ? WHERE id = ?",
            (dispositivo.get_nombre_dispositivo(), dispositivo.get_tipo(), estado_int, dispositivo.get_id())
        )
        conn.commit()

    def eliminar(self, dispositivo):
        if dispositivo.get_id() is None:
            raise ValueError("Dispositivo debe tener un ID para eliminarlo")
        cursor.execute("DELETE FROM dispositivos WHERE id = ?", (dispositivo.get_id(),))
        conn.commit()

    def obtener_por_id(self, id):
        cursor.execute("SELECT * FROM dispositivos WHERE id = ?", (id,))
        fila = cursor.fetchone()
        if fila:
            return Dispositivo(fila[1], fila[2], bool(fila[3]), id=fila[0])
        return None

