from dao.interfaces.i_usuario_dao import IUsuarioDAO
from dominio.usuario import Usuario
from conn.db_conn import conn, cursor

class UsuarioDAO(IUsuarioDAO):
    def guardar(self, usuario: Usuario):
        cursor.execute(
            "INSERT INTO usuarios (nombre, email, password, rol) VALUES (?, ?, ?, ?)",
            (usuario.nombre, usuario.email, usuario.password, usuario.rol)
        )
        conn.commit()
        return cursor.lastrowid

    def obtener_por_id(self, id: int):
        cursor.execute("SELECT * FROM usuarios WHERE id=?", (id,))
        fila = cursor.fetchone()
        if fila:
            return Usuario(fila[1], fila[2], fila[3], fila[4])
        return None

    def listar(self):
        cursor.execute("SELECT * FROM usuarios")
        return cursor.fetchall()

    def modificar(self, usuario: Usuario):
        cursor.execute(
            "UPDATE usuarios SET nombre=?, email=?, password=?, rol=? WHERE email=?",
            (usuario.nombre, usuario.email, usuario.password, usuario.rol, usuario.email)
        )
        conn.commit()

    def eliminar(self, usuario: Usuario):
        cursor.execute("DELETE FROM usuarios WHERE email=?", (usuario.email,))
        conn.commit()
