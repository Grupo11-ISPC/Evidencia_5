from dominio.usuario import Usuario
from dominio.dispositivo import Dispositivo
from dao.usuario_dao import UsuarioDAO
from dao.dispositivo_dao import DispositivoDAO
import os

# Variables globales
usuario_actual = None
usuario_dao = UsuarioDAO()
dispositivo_dao = DispositivoDAO()

###################################################################################
# Menú principal
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
                if usuario_actual.get_rol() == "admin": # type: ignore
                    menu_admin()
                else:
                    menu_usuario()
        elif opcion == "0":
            print("Hasta luego")
            break
        else:
            print("Opción inválida")
            pausar()

####################################### OPCIÓN 1 #############################################
def registrar_usuario():
    limpiar()
    print("REGISTRO DE USUARIO")
    nombre = pedir_dato("Nombre: ")

    while True:
        email = input("Email: ").strip()
        if not email:
            print("Error: el correo no puede estar vacío")
        elif "@" not in email or "." not in email:
            print("Error: el correo debe contener '@' y '.'")
        else:
            break
        
    while True:
        password = pedir_dato("Password (min 6 caracteres): ")
        if len(password) < 6:
            print("Error: la contraseña debe tener al menos 6 caracteres")
        else:
            break
        
    # Si no hay usuarios, el primero será admin
    rol = "admin" if len(usuario_dao.listar_usuarios()) == 0 else "user" # type: ignore

    if not Usuario.validar_usuario(nombre, email, password, rol):
        print("Datos inválidos: revisa nombre, email, contraseña o rol")
        pausar()
        return
    
    usuario = Usuario(nombre, email, password, rol)
    id_nuevo = usuario_dao.crear_usuario(usuario)

    if id_nuevo:
        print(f"Usuario {nombre} registrado como {rol}")
    else:
        print("No se pudo registrar el usuario (el email ya existe o hubo un error)")

    pausar()

#################################### OPCIÓN 2 ################################################
# Inicio de sesión
def iniciar_sesion():
    global usuario_actual
    limpiar()
    print("INICIO DE SESIÓN")
    email = input("Email: ").strip()
    password = input("Contraseña: ").strip()
    usuarios = usuario_dao.listar_usuarios()

    for u in usuarios:  # type: ignore
        if u.get_email() == email and u.get_password() == password:
            usuario_actual = u
            print(f"👋Bienvenido, {usuario_actual.get_nombre()}!")
            pausar()
            return True
    print("Email o contraseña incorrectos")
    pausar()

###################################################################################
# Menús
def menu_usuario():
    while True:
        limpiar()
        print(f"MENU USUARIO - {usuario_actual.get_nombre()}") # type: ignore
        print("1. Consultar datos personales")
        print("2. Consultar dispositivos")
        print("0. Cerrar sesión")
        opcion = input("Opción: ")

        if opcion == "1":
            limpiar()
            print(f"Nombre: {usuario_actual.get_nombre()}") # type: ignore
            print(f"Email: {usuario_actual.get_email()}") # type: ignore
            print(f"Rol: {usuario_actual.get_rol()}") # type: ignore
            pausar()
        elif opcion == "2":
            limpiar()   
            dispositivos = dispositivo_dao.listar_dispositivos()
            if not dispositivos:
                print("No hay dispositivos.")
            else:
                for i, d in enumerate(dispositivos, 1):
                    print(f"{i}. {d.get_nombre_dispositivo()} ({d.get_tipo_dispositivo()}) - Estado: {'Encendido' if d.get_estado_dispositivo() else 'Apagado'}")
            pausar()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")
            pausar()

def menu_admin():
    while True:
        limpiar()
        print(f"MENU ADMIN - {usuario_actual.get_nombre()}") # type: ignore
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
            dispositivo = Dispositivo(nombre, tipo)
            dispositivo_dao.crear_dispositivo(dispositivo, usuario_actual.get_id()) # type: ignore
            print("Dispositivo agregado")
            pausar()

        elif opcion == "2":
            limpiar()
            dispositivos = dispositivo_dao.listar_dispositivos()
            if not dispositivos:
                print("No hay dispositivos.")
            else:
                for i, d in enumerate(dispositivos, 1):
                    print(f"{i}. {d.get_nombre_dispositivo()} ({d.get_tipo_dispositivo()}) - Estado: {'Encendido' if d.get_estado_dispositivo() else 'Apagado'}")
            pausar()

        elif opcion == "3":
            limpiar()
            dispositivos = dispositivo_dao.listar_dispositivos()
            if not dispositivos:
                print("No hay dispositivos para modificar.")
                pausar()
                continue

            for i, d in enumerate(dispositivos, 1):
                print(f"{i}. {d.get_nombre_dispositivo()} ({d.get_tipo_dispositivo()})")

            try:
                idx = int(input("Número de dispositivo a modificar: ")) - 1
                if 0 <= idx < len(dispositivos):
                    d = dispositivos[idx]
                    nuevo_nombre = input("Nuevo nombre (enter para mantener): ").strip() or d.get_nombre_dispositivo()
                    nuevo_tipo = input("Nuevo tipo (enter para mantener): ").strip() or d.get_tipo_dispositivo()

                    disp = Dispositivo(nuevo_nombre, nuevo_tipo, d.get_estado_dispositivo(), id=d.get_id())
                    dispositivo_dao.modificar_dispositivo(disp)
                    print("✅ Dispositivo modificado")
                else:
                    print("Número inválido")
            except ValueError:
                print("Entrada inválida")
            pausar()

        elif opcion == "4":
            limpiar()
            dispositivos = dispositivo_dao.listar_dispositivos()
            if not dispositivos:
                print("No hay dispositivos para eliminar.")
                pausar()
                continue

            for i, d in enumerate(dispositivos, 1):
                print(f"{i}. {d.get_nombre_dispositivo()} ({d.get_tipo_dispositivo()})")

            try:
                idx = int(input("Número de dispositivo a eliminar: ")) - 1
                if 0 <= idx < len(dispositivos):
                    d = dispositivos[idx]
                    dispositivo_dao.eliminar_dispositivo(d.get_id())
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
    usuarios = usuario_dao.listar_usuarios()  # type: ignore

    # Evita el error de tipo (usuarios podría ser None)
    if not usuarios:
        print("No hay usuarios registrados.")
        pausar()
        return

    # Muestra los usuarios correctamente
    for i, u in enumerate(usuarios, 1):
        print(f"{i}. {u.get_nombre()} ({u.get_email()}) - Rol: {u.get_rol()}")

    try:
        num = int(input("Número de usuario: ")) - 1
        if 0 <= num < len(usuarios):
            seleccionado = usuarios[num]

            # Evita cambiar tu propio rol
            if seleccionado.get_email() == usuario_actual.get_email():  # type: ignore
                print("No puedes cambiar tu propio rol")
            else:
                nuevo_rol = input("Nuevo rol (admin/user): ").strip().lower()
                if nuevo_rol not in ("admin", "user"):
                    print("Rol inválido. Usa 'admin' o 'user'.")
                    pausar()
                    return

                # Crear un nuevo objeto con el nuevo rol
                usuario_obj = Usuario(
                    nombre=seleccionado.get_nombre(),
                    email=seleccionado.get_email(),
                    password=seleccionado.get_password(),
                    rol=nuevo_rol,
                    id=seleccionado.get_id()
                )

                if usuario_dao.modificar_usuario(usuario_obj):  # type: ignore
                    print(f"Rol cambiado a '{nuevo_rol}' para {seleccionado.get_nombre()}")
                else:
                    print("Error al actualizar el rol.")
        else:
            print("Número fuera de rango")

    except ValueError:
        print("Entrada inválida")

    pausar()

#################################################################################################################
#validador de ingreso de datos
def pedir_dato(mensaje):
    while True:
        valor = input(mensaje).strip() 
        if not valor: 
            print("Error: el dato no puede estar vacío.")
        else:
            return valor

# Helpers
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPresiona Enter para continuar...")

###################################################################################
if __name__ == "__main__":
    main()