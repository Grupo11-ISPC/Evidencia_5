from conn.db_conn import ConexionDB
from dominio.dispositivo import Dispositivo
from dao.interfaces.i_dispositivo_dao import IDispositivoDAO


class DispositivoDAO(IDispositivoDAO):

    def crear_dispositivo(self, dispositivo, id_usuario):
        conexion = None
        cursor = None
        try:
            conexion = ConexionDB.get_conexion()
            if conexion:
                cursor = conexion.cursor()
                sql = """
                    INSERT INTO dispositivos (nombre, tipo, estado, id_usuario)
                    VALUES (%s, %s, %s, %s)
                """
                valores = (
                    dispositivo.get_nombre(),
                    dispositivo.get_tipo(),
                    dispositivo.get_estado(),
                    id_usuario
                )
                cursor.execute(sql, valores)
                conexion.commit()

                dispositivo.__id = cursor.lastrowid
                print(f"Dispositivo '{dispositivo.get_nombre()}' creado con ID: {dispositivo.__id}")
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

    def obtener_por_id(self, id: int):
        conexion = None
        cursor = None
        try:
            conexion = ConexionDB.get_conexion()
            if conexion:
                cursor = conexion.cursor()
                sql = """
                    SELECT id, nombre, tipo, estado
                    FROM dispositivos
                    WHERE id = %s
                """
                cursor.execute(sql, (id,))
                fila = cursor.fetchone()

                if fila:
                    dispositivo = Dispositivo(
                        nombre=fila[1],#type: ignore
                        tipo=fila[2],#type: ignore
                        estado=bool(fila[3]),#type: ignore
                        id=fila[0] #type: ignore
                    )
                    return dispositivo
                else:
                    print(f"No se encontró dispositivo con ID: {id}")
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
        conexion = None
        cursor = None
        try:
            conexion = ConexionDB.get_conexion()
            if conexion:
                cursor = conexion.cursor()
                sql = """
                    UPDATE dispositivos
                    SET nombre = %s, tipo = %s, estado = %s
                    WHERE id = %s
                """
                valores = (
                    dispositivo.get_nombre(),
                    dispositivo.get_tipo(),
                    dispositivo.get_estado(),
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

    def eliminar_dispositivo(self, id: int):
        conexion = None
        cursor = None
        try:
            conexion = ConexionDB.get_conexion()
            if conexion:
                cursor = conexion.cursor()
                sql = "DELETE FROM dispositivos WHERE id = %s"
                cursor.execute(sql, (id,))
                conexion.commit()

                if cursor.rowcount > 0:
                    print(f"Dispositivo ID {id} eliminado")
                    return True
                else:
                    print(f"No se encontró dispositivo con ID: {id}")
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

    def cambiar_estado(self, id: int, nuevo_estado: bool):
        conexion = None
        cursor = None
        try:
            conexion = ConexionDB.get_conexion()
            if conexion:
                cursor = conexion.cursor()
                sql = "UPDATE dispositivos SET estado = %s WHERE id = %s"
                cursor.execute(sql, (nuevo_estado, id))
                conexion.commit()

                if cursor.rowcount > 0:
                    estado_texto = "encendido" if nuevo_estado else "apagado"
                    print(f"✅ Dispositivo ID {id} {estado_texto}")
                    return True
                else:
                    print(f"⚠️ No se encontró dispositivo con ID: {id}")
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
                sql = "SELECT id, nombre, tipo, estado FROM dispositivos"
                cursor.execute(sql)
                filas = cursor.fetchall()

                for fila in filas:
                    dispositivos.append(
                        Dispositivo(
                            nombre=fila[1], # type: ignore
                            tipo=fila[2], # type: ignore
                            estado=bool(fila[3]), # type: ignore
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
                    SET nombre = %s, tipo = %s, estado = %s
                    WHERE id = %s
                """
                valores = (
                    dispositivo.get_nombre(),
                    dispositivo.get_tipo(),
                    dispositivo.get_estado(),
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

    def get_nombre_dispositivo(self, id: int):
        raise NotImplementedError