from conn.db_conn import ConexionDB
from typing import Optional
from dominio.usuario import Usuario
from dao.interfaces.i_usuario_dao import IUsuarioDAO

class UsuarioDAO(IUsuarioDAO):
    def crear_usuario(self, usuario):
        conexion = None
        try:
            conexion = ConexionDB.get_conexion()
            if conexion:
                cursor = conexion.cursor()
                
                sql = """
                    INSERT INTO usuarios (nombre, email, password, rol) 
                    VALUES (%s, %s, %s, %s)
                """
                valores = (
                    usuario.get_nombre(),
                    usuario.get_email(),
                    usuario._password,
                    usuario.get_rol()
                )
                
                cursor.execute(sql, valores)
                conexion.commit()
                
                # Obtener el ID generado
                usuario._id = cursor.lastrowid
                
                print(f"Usuario '{usuario.get_nombre()}' creado con ID: {usuario._id}")
                return True
                
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            if conexion:
                conexion.rollback()
            return False
            
        finally:
            if conexion:
                cursor.close()
                ConexionDB.cerrar_conexion(conexion)
    def obtener_por_id(self, id):
        """Busca y devuelve un usuario por su ID"""
        conexion = None
        try:
            conexion = ConexionDB.get_conexion()
            if conexion:
                cursor = conexion.cursor()
                
                sql = "SELECT id, nombre, email, password, rol FROM usuarios WHERE id = %s"
                cursor.execute(sql, (id,))
                
                fila = cursor.fetchall()
                
                if fila:
                    # Crear objeto Usuario con los datos de la BD
                    usuario = Usuario(
                        nombre=fila[1],
                        email=fila[2],
                        password=fila[3],
                        rol=fila[4],
                        id=fila[0]
                    )
                    return usuario
                else:
                    print(f"No se encontró usuario con ID: {id}")
                    return None
                    
        except Exception as e:
            print(f"Error al obtener usuario: {e}")
            return None
            
        finally:
            if conexion:
                cursor.close()
                ConexionDB.cerrar_conexion(conexion)
    def obtener_por_email(self, email):
        raise NotImplementedError
    def eliminar(self, id):
        """Elimina un usuario de la base de datos"""
        conexion = None
        try:
            conexion = ConexionDB.get_conexion()
            if conexion:
                cursor = conexion.cursor()
                
                sql = "DELETE FROM usuarios WHERE id = %s"
                cursor.execute(sql, (id,))
                conexion.commit()
                
                if cursor.rowcount > 0:
                    print(f"Usuario ID {id} eliminado")
                    return True
                else:
                    print(f"No se encontró usuario con ID: {id}")
                    return False
                    
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            if conexion:
                conexion.rollback()
            return False
            
        finally:
            if conexion:
                cursor.close()
                ConexionDB.cerrar_conexion(conexion)
    def listar_usuarios(self):
        conexion = None
        usuarios = []
        try:
            conexion = ConexionDB.get_conexion()
            if conexion:
                cursor = conexion.cursor()
                
                sql = "SELECT id, nombre, email, password, rol FROM usuarios"
                cursor.execute(sql)
                
                filas = cursor.fetchall()
                
                for fila in filas: 
                    usuario = Usuario(
                        nombre=fila[1], #type: ignore
                        email=fila[2],#type: ignore
                        password=fila[3],#type: ignore
                        rol=fila[4],#type: ignore
                        id=fila[0]#type: ignore
                    )
                    usuarios.append(usuario)
                return usuarios
                    
        except Exception as e:
            print(f"Error al listar usuarios: {e}")
            return []
            
        finally:
            if conexion:
                cursor.close()
                ConexionDB.cerrar_conexion(conexion)
    def modificar_usuario(self, usuario: Usuario):
        conexion = None
        cursor = None
        try:
            conexion = ConexionDB.get_conexion()
            if conexion:
                cursor = conexion.cursor()
                sql = """
                    UPDATE usuarios 
                    SET nombre = %s, email = %s, password = %s, rol = %s
                    WHERE id = %s
                """
                valores = (
                    usuario.get_nombre(),
                    usuario.get_email(),
                    usuario._password,
                    usuario.get_rol(),
                    usuario.get_id()
                )
                
                cursor.execute(sql, valores)
                conexion.commit()
                
                if cursor.rowcount > 0:
                    print(f"Usuario ID {usuario.get_id()} modificado")
                    return True
                else:
                    print(f"No se encontró usuario con ID: {usuario.get_id()}")
                    return False
        except Exception as e:
            print(f"Error al modificar usuario: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if cursor:
                cursor.close()
            if conexion:
                ConexionDB.cerrar_conexion(conexion)
    def obtener_usuario_por_id(self, usuario_id: int) -> Optional[Usuario]:
        raise NotImplementedError   
    def eliminar_usuario(self, usuario_id: int):
        raise NotImplementedError