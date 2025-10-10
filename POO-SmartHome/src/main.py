from usuario import Usuario
from dispositivo import Dispositivo
from accion import Accion
import os

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPresioná Enter para continuar...")

# Variables globales
usuarios = []
usuario_actual = None

# ========== REGISTRO E INICIO DE SESIÓN ==========

def registrar_usuario():
    limpiar()
    print("=== REGISTRO ===")
    nombre = input("Nombre: ").strip()
    email = input("Email: ").strip()
    password = input("Password: ").strip()
    
    # Primer usuario es admin
    if len(usuarios) == 0:
        rol = "admin"
        print("\n✓ Primer usuario registrado como ADMIN")
    else:
        rol = "usuario"
        print("\n✓ Registrado como usuario estándar")
    
    try:
        usuario = Usuario(nombre, email, password, rol)
        usuarios.append(usuario)
        print(f"✓ {nombre} registrado exitosamente")
    except ValueError as e:
        print(f"❌ Error: {e}")

def iniciar_sesion():
    global usuario_actual
    limpiar()
    print("=== INICIAR SESIÓN ===")
    email = input("Email: ").strip()
    password = input("Password: ").strip()
    
    for usuario in usuarios:
        if usuario.get_email() == email and usuario.password == password:
            usuario_actual = usuario
            print(f"\n✓ Bienvenido {usuario.get_nombre()}")
            pausar()
            return True
    
    print("\n❌ Credenciales incorrectas")
    pausar()
    return False

# ========== MENÚ USUARIO ESTÁNDAR ==========

def consultar_datos_personales():
    limpiar()
    print("=== DATOS PERSONALES ===\n")
    print(f"Nombre: {usuario_actual.get_nombre()}")
    print(f"Email: {usuario_actual.get_email()}")
    print(f"Rol: {usuario_actual.get_rol()}")
    print(f"Dispositivos: {len(usuario_actual.dispositivos)}")

def consultar_dispositivos():
    limpiar()
    print("=== MIS DISPOSITIVOS ===\n")
    if not usuario_actual.dispositivos:
        print("No hay dispositivos registrados")
    else:
        for i, disp in enumerate(usuario_actual.dispositivos, 1):
            print(f"{i}. {disp}")

def menu_estandar():
    global usuario_actual
    while True:
        limpiar()
        print(f"=== MENÚ USUARIO - {usuario_actual.get_nombre()} ===")
        print("\n1. Consultar datos personales")
        print("2. Consultar dispositivos")
        print("0. Cerrar sesión")
        
        opcion = input("\nOpción: ")
        
        if opcion == "1":
            consultar_datos_personales()
            pausar()
        elif opcion == "2":
            consultar_dispositivos()
            pausar()
        elif opcion == "0":
            usuario_actual = None
            break
        else:
            print("❌ Opción inválida")
            pausar()

#
#Para hacer el menú de admin...



# ========== MENÚ PRINCIPAL ==========

def main():
    while True:
        limpiar()
        print("=== SMART HOME ===")
        print("\n1. Registrar usuario")
        print("2. Iniciar sesión")
        print("0. Salir")
        
        opcion = input("\nOpción: ")
        
        if opcion == "1":
            registrar_usuario()
            pausar()
        elif opcion == "2":
            if iniciar_sesion():
                if usuario_actual.get_rol() == "admin":
                    menu_admin()
                else:
                    menu_estandar()
        elif opcion == "0":
            print("\n👋 Hasta luego!")
            break
        else:
            print("❌ Opción inválida")
            pausar()

if __name__ == "__main__":
    main()