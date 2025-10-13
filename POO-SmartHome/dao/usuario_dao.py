import sqlite3
from dao.interfaces.i_usuario_dao import IUsuarioDAO
from dominio.usuario import Usuario
from conn.db_conn import conn, cursor

class UsuarioDAO(IUsuarioDAO):
    def guardar(self, usuario: Usuario):
        try:
            cursor.execute(
                "INSERT INTO usuarios (nombre, email, password, rol) VALUES (?, ?, ?, ?)",
                (usuario.get_nombre(), usuario.get_email(), usuario._Usuario__password, usuario.get_rol())
            )
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error  as e:
            print("Error al guardar usuario:")
            conn.rollback()
            return None

    def obtener_por_id(self, id: int):
        try:
            cursor.execute("SELECT * FROM usuarios WHERE id=?", (id,))
            fila = cursor.fetchone()
            if fila:
                return Usuario(fila[1], fila[2], fila[3], fila[4], id=fila[0])
            return None
        except sqlite3.Error as e:
            print(f"Error al obtener usuario por ID: {e}")
            return None

    def listar(self):
        try:
            cursor.execute("SELECT * FROM usuarios")
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error al listar usuarios: {e}")
            return []

    def modificar(self, usuario: Usuario):
        try:
            cursor.execute(
                "UPDATE usuarios SET nombre=?, email=?, password=?, rol=? WHERE email=?",
                (usuario.get_nombre(), usuario.get_email(), usuario._Usuario__password, usuario.get_rol(), usuario.get_email())
            )
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error al modificar usuario: {e}")
            conn.rollback()

    def eliminar(self, usuario: Usuario):
        try:
            cursor.execute("DELETE FROM usuarios WHERE email=?", (usuario.get_email(),))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error al eliminar usuario: {e}")
            conn.rollback()