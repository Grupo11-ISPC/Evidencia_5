from dominio.usuario import Usuario
from dominio.dispositivo import Dispositivo
from dominio.automatizacion import Automatizacion
from dominio.accion import Accion

from dao.usuario_dao import UsuarioDAO
from dao.dispositivo_dao import DispositivoDAO
from conn.db_conn import conn, cursor
import os

# Helpers
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPresiona Enter para continuar...")

# Variables globales
usuario_actual = None
usuario_dao = UsuarioDAO()
dispositivo_dao = DispositivoDAO()

#validador de ingreso de datos
def pedir_dato(mensaje):
    while True:
        valor = input(mensaje).strip() 
        if not valor: 
            print("Error: el dato no puede estar vacío.")
        else:
            return valor


# Registro e inicio de sesión
def registrar_usuario():
    limpiar()
    print("REGISTRO DE USUARIO")
    nombre = pedir_dato("Nombre: ")

#valiador ingreso mail correcto
    while True:
        email = input("Email: ").strip()
        if not email:
            print("Error: el correo no puede estar vacío")
        elif "@" not in email or "." not in email:
            print("Error: el correo debe contener '@' y '.'")
        else:
            print("Correo válido:", email)
            break

#validador de caracteres de contraseña
    while True:
        password = pedir_dato("Password (min 6 caracteres): ")#con pedir_dato()valido que no sea vacio
        if len(password)<6:
            print("Error: la contraseña debe tener al menos 6 caracteres")
        else:
            print("contraseña valida")
            break
        
    rol = "admin" if len(usuario_dao.listar()) == 0 else "user"

    try:
        usuario = Usuario(nombre, email, password, rol)
        usuario_dao.guardar(usuario)
        print(f"Usuario {nombre} registrado como {rol}")
    except ValueError as e:
        print(f"Error: {e}")
    pausar()

def iniciar_sesion():
    global usuario_actual
    limpiar()
    print("INICIO DE SESIÓN")
    email = input("Email: ").strip()
    password = input("Password: ").strip()
    usuarios = usuario_dao.listar()

    for fila in usuarios:
        id, nombre, mail, pwd, rol = fila
        if mail == email and pwd == password:
            usuario_actual = Usuario(nombre, mail, pwd, rol, id)
            print(f"Bienvenido {nombre}")
            pausar()
            return True

    print("Credenciales incorrectas")
    pausar()
    return False

# Menús
def menu_usuario():
    while True:
        limpiar()
        print(f"MENU USUARIO - {usuario_actual.get_nombre()}")
        print("1. Consultar datos personales")
        print("2. Consultar dispositivos")
        print("0. Cerrar sesión")
        opcion = input("Opción: ")

        if opcion == "1":
            limpiar()
            print(f"Nombre: {usuario_actual.get_nombre()}")
            print(f"Email: {usuario_actual.get_email()}")
            print(f"Rol: {usuario_actual.get_rol()}")
            pausar()
        elif opcion == "2":
            limpiar()
            dispositivos = dispositivo_dao.listar()
            if not dispositivos:
                print("No hay dispositivos.")
            else:
                for i, d in enumerate(dispositivos, 1):
                    print(f"{i}. {d[1]} ({d[2]}) - Estado: {'Encendido' if d[3] else 'Apagado'}")
            pausar()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")
            pausar()

def menu_admin():
    while True:
        limpiar()
        print(f"MENU ADMIN - {usuario_actual.get_nombre()}")
        print("1. Gestionar dispositivos")
        print("2. Cambiar rol de usuario")
        print("0. Cerrar sesión")
        opcion = input("Opción: ")

        if opcion == "1":
            gestionar_dispositivos()
        elif opcion == "2":
            cambiar_rol()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")
            pausar()

# Funciones admin
def gestionar_dispositivos():
    while True:
        limpiar()
        print("GESTIÓN DE DISPOSITIVOS")
        print("1. Agregar")
        print("2. Listar")
        print("3. Modificar")
        print("4. Eliminar")
        print("0. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            limpiar()
            nombre = input("Nombre: ").strip()
            tipo = input("Tipo: ").strip()
            disp = Dispositivo(nombre, tipo)
            dispositivo_dao.guardar(disp)
            print("Dispositivo agregado")
            pausar()

        elif opcion == "2":
            limpiar()
            dispositivos = dispositivo_dao.listar()
            if not dispositivos:
                print("No hay dispositivos.")
            else:
                for i, d in enumerate(dispositivos, 1):
                    print(f"{i}. {d[1]} ({d[2]}) - Estado: {'Encendido' if d[3] else 'Apagado'}")
            pausar()

        elif opcion == "3":
            limpiar()
            dispositivos = dispositivo_dao.listar()
            if not dispositivos:
                print("No hay dispositivos para modificar.")
                pausar()
                continue

            for i, d in enumerate(dispositivos, 1):
                print(f"{i}. {d[1]} ({d[2]})")
            try:
                idx = int(input("Número de dispositivo a modificar: ")) - 1
                if 0 <= idx < len(dispositivos):
                    d = dispositivos[idx]
                    nuevo_nombre = input("Nuevo nombre: ").strip()
                    nuevo_tipo = input("Nuevo tipo: ").strip()
                    # Creamos el objeto con el ID existente
                    disp = Dispositivo(nuevo_nombre, nuevo_tipo, bool(d[3]), id=d[0])
                    dispositivo_dao.modificar(disp)
                    print("Dispositivo modificado")
                else:
                    print("Dispositivo no encontrado")
            except ValueError:
                print("Entrada inválida")
            pausar()

        elif opcion == "4":
            limpiar()
            dispositivos = dispositivo_dao.listar()
            if not dispositivos:
                print("No hay dispositivos para eliminar.")
                pausar()
                continue

            for i, d in enumerate(dispositivos, 1):
                print(f"{i}. {d[1]} ({d[2]})")
            try:
                idx = int(input("Número de dispositivo a eliminar: ")) - 1
                if 0 <= idx < len(dispositivos):
                    d = dispositivos[idx]
                    # Creamos el objeto con el ID para que el DAO lo pueda eliminar
                    disp = Dispositivo(d[1], d[2], bool(d[3]), id=d[0])
                    dispositivo_dao.eliminar(disp)
                    print("Dispositivo eliminado")
                else:
                    print("Dispositivo no encontrado")
            except ValueError:
                print("Entrada inválida")
            pausar()

        elif opcion == "0":
            break

        else:
            print("Opción inválida")
            pausar()


def cambiar_rol():
    limpiar()
    usuarios = usuario_dao.listar()
    for i, u in enumerate(usuarios, 1):
        print(f"{i}. {u[1]} ({u[2]}) - Rol: {u[4]}")
    try:
        num = int(input("Número de usuario: ")) - 1
        if 0 <= num < len(usuarios):
            seleccionado = usuarios[num]
            if seleccionado[2] == usuario_actual.get_email():
                print("No puedes cambiar tu propio rol")
            else:
                nuevo_rol = input("Nuevo rol (admin/user): ").strip()
                usuario_obj = Usuario(seleccionado[1], seleccionado[2], seleccionado[3], nuevo_rol, seleccionado[0])
                usuario_dao.modificar(usuario_obj)
                print("Rol cambiado")
    except:
        print("Entrada inválida")
    pausar()

# Main
def main():
    while True:
        limpiar()
        print("SMART HOME")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("0. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            if iniciar_sesion():
                if usuario_actual.get_rol() == "admin":
                    menu_admin()
                else:
                    menu_usuario()
        elif opcion == "0":
            print("Hasta luego")
            break
        else:
            print("Opción inválida")
            pausar()

if __name__ == "__main__":
    main()