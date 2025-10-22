from conn.db_conn import ConexionDB
from dominio.dispositivo import Dispositivo
from dao.interfaces.i_dispositivo_dao import IDispositivoDAO


class DispositivoDAO(IDispositivoDAO):
    """Implementación del DAO para Dispositivo"""

    def crear_dispositivo(self, dispositivo, id_usuario):
        """Guarda un nuevo dispositivo asociado a un usuario"""
        conexion = None
        cursor = None
        try:
            conexion = ConexionDB.get_conexion()
            if conexion:
                cursor = conexion.cursor()
                sql = """
                    INSERT INTO dispositivos (nombre_dispositivo, tipo_dispositivo, estado_dispositivo, id_usuario)
                    VALUES (%s, %s, %s, %s)
                """
                valores = (
                    dispositivo.get_nombre_dispositivo(),
                    dispositivo.get_tipo_dispositivo(),
                    dispositivo.get_estado_dispositivo(),
                    id_usuario
                )
                cursor.execute(sql, valores)
                conexion.commit()

                dispositivo._id = cursor.lastrowid
                print(f"Dispositivo '{dispositivo.get_nombre_dispositivo()}' creado con ID: {dispositivo._id}")
                return True

        except Exception as e:
            print(f"Error al crear dispositivo: {e}")
            if conexion:
                conexion.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            if conexion:
                ConexionDB.cerrar_conexion(conexion)

    def obtener_por_id(self, id_dispositivo: int):
        conexion = None
        cursor = None
        try:
            conexion = ConexionDB.get_conexion()
            if conexion:
                cursor = conexion.cursor()
                sql = """
                    SELECT id, nombre_dispositivo, tipo_dispositivo, estado_dispositivo
                    FROM dispositivos
                    WHERE id = %s
                """
                cursor.execute(sql, (id_dispositivo,))
                fila = cursor.fetchall() 

                if fila:
                    dispositivo = Dispositivo(
                        nombre_dispositivo=fila[1],
                        tipo_dispositivo=fila[2],
                        estado_dispositivo=bool(fila[3]),
                        id=fila[0]
                    )
                    return dispositivo
                else:
                    print(f"No se encontró dispositivo con ID: {id_dispositivo}")
                    return None

        except Exception as e:
            print(f"Error al obtener dispositivo: {e}")
            return None

        finally:
            if cursor:
                cursor.close()
            if conexion:
                ConexionDB.cerrar_conexion(conexion)

    def actualizar_dispositivo(self, dispositivo):
        """Actualiza los datos de un dispositivo existente"""
        conexion = None
        cursor = None
        try:
            conexion = ConexionDB.get_conexion()
            if conexion:
                cursor = conexion.cursor()
                sql = """
                    UPDATE dispositivos
                    SET nombre_dispositivo = %s, tipo_dispositivo = %s, estado_dispositivo = %s
                    WHERE id = %s
                """
                valores = (
                    dispositivo.get_nombre_dispositivo(),
                    dispositivo.get_tipo_dispositivo(),
                    dispositivo.get_estado_dispositivo(),
                    dispositivo.get_id()
                )
                cursor.execute(sql, valores)
                conexion.commit()

                if cursor.rowcount > 0:
                    print(f"Dispositivo ID {dispositivo.get_id()} actualizado")
                    return True
                else:
                    print(f"No se encontró dispositivo con ID: {dispositivo.get_id()}")
                    return False

        except Exception as e:
            print(f"Error al actualizar dispositivo: {e}")
            if conexion:
                conexion.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            if conexion:
                ConexionDB.cerrar_conexion(conexion)

    def eliminar_dispositivo(self, id_dispositivo: int):
        """Elimina un dispositivo de la base de datos"""
        conexion = None
        cursor = None
        try:
            conexion = ConexionDB.get_conexion()
            if conexion:
                cursor = conexion.cursor()
                sql = "DELETE FROM dispositivos WHERE id = %s"
                cursor.execute(sql, (id_dispositivo,))
                conexion.commit()

                if cursor.rowcount > 0:
                    print(f"Dispositivo ID {id_dispositivo} eliminado")
                    return True
                else:
                    print(f"No se encontró dispositivo con ID: {id_dispositivo}")
                    return False

        except Exception as e:
            print(f"Error al eliminar dispositivo: {e}")
            if conexion:
                conexion.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            if conexion:
                ConexionDB.cerrar_conexion(conexion)

    def cambiar_estado(self, id_dispositivo: int, nuevo_estado: bool):
        """Cambia el estado de un dispositivo (encendido/apagado)"""
        conexion = None
        cursor = None
        try:
            conexion = ConexionDB.get_conexion()
            if conexion:
                cursor = conexion.cursor()
                sql = "UPDATE dispositivos SET estado_dispositivo = %s WHERE id = %s"
                cursor.execute(sql, (nuevo_estado, id_dispositivo))
                conexion.commit()

                if cursor.rowcount > 0:
                    estado_texto = "encendido" if nuevo_estado else "apagado"
                    print(f"✅ Dispositivo ID {id_dispositivo} {estado_texto}")
                    return True
                else:
                    print(f"⚠️ No se encontró dispositivo con ID: {id_dispositivo}")
                    return False

        except Exception as e:
            print(f"Error al cambiar estado: {e}")
            if conexion:
                conexion.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            if conexion:
                ConexionDB.cerrar_conexion(conexion)

    def listar_dispositivos(self):
        conexion = None
        cursor = None
        dispositivos = []   
        try:
            conexion = ConexionDB.get_conexion()
            if conexion:
                cursor = conexion.cursor()
                sql = "SELECT id, nombre_dispositivo, tipo_dispositivo, estado_dispositivo FROM dispositivos"
                cursor.execute(sql)
                filas = cursor.fetchall()

                for fila in filas:
                    dispositivos.append(
                        Dispositivo(
                            nombre_dispositivo=fila[1], # type: ignore
                            tipo_dispositivo=fila[2], # type: ignore
                            estado_dispositivo=bool(fila[3]), # type: ignore
                            id=fila[0] # type: ignore
                        )
                    )

                return dispositivos

        except Exception as e:
            print(f"Error al listar dispositivos: {e}")
            return []

        finally:
            if cursor:
                cursor.close()
            if conexion:
                ConexionDB.cerrar_conexion(conexion)

    def modificar_dispositivo(self, dispositivo: Dispositivo):
        conexion = None
        cursor = None
        try:
            conexion = ConexionDB.get_conexion()
            if conexion:
                cursor = conexion.cursor()
                sql = """
                    UPDATE dispositivos
                    SET nombre_dispositivo = %s, tipo_dispositivo = %s, estado_dispositivo = %s
                    WHERE id = %s
                """
                valores = (
                    dispositivo.get_nombre_dispositivo(),
                    dispositivo.get_tipo_dispositivo(),
                    dispositivo.get_estado_dispositivo(),
                    dispositivo.get_id()
                )
                cursor.execute(sql, valores)
                conexion.commit()

                if cursor.rowcount > 0:
                    print(f"Dispositivo ID {dispositivo.get_id()} modificado")
                    return True
                else:
                    print(f"No se encontró dispositivo con ID: {dispositivo.get_id()}")
                    return False
        except Exception as e:
            print(f"Error al modificar dispositivo: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if cursor:
                cursor.close()
            if conexion:
                ConexionDB.cerrar_conexion(conexion)

    def listar_dispositivo(self):
        raise NotImplementedError

    def get_nombre_dispositivo(self, id_dispositivo: int):
        raise NotImplementedError