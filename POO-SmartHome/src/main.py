from usuario import Usuario
from dispositivo import Dispositivo
import os

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPresioná Enter para continuar...")

# Variables globales
usuarios = []
usuario_actual = None
dispositivos_compartidos = []

# ========== REGISTRO E INICIO DE SESIÓN ==========

def registrar_usuario():
    while True:
        limpiar()
        print("=== REGISTRO ===")
        nombre = input("Nombre: ").strip()
        
        if not nombre:
            print("❌ El nombre no puede estar vacío")
            pausar()
            continue
        
        email = input("Email: ").strip()
        # Validar formato de email
        if not email or "@" not in email or "." not in email.split("@")[-1]:
            print("❌ Email inválido. Debe contener @ y un dominio válido (ej: usuario@email.com)")
            pausar()
            continue
        
        password = input("Password (mín 6 caracteres): ").strip()
        
        if len(password) < 6:
            print("❌ La contraseña debe tener al menos 6 caracteres")
            pausar()
            continue
    
        # Primer usuario es admin
        if len(usuarios) == 0:
            rol = "admin"
            print("\n✓ Primer usuario registrado como ADMIN")
        else:
            rol = "user"
            print("\n✓ Registrado como usuario estándar")
        
        try:
            usuario = Usuario(nombre, email, password, rol)
            usuarios.append(usuario)
            print(f"✓ {nombre} registrado exitosamente")
            break
        except ValueError as e:
            print(f"❌ Error: {e}")
            pausar()

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
    print(f"Dispositivos compartidos: {len(dispositivos_compartidos)}")

def consultar_dispositivos():
    limpiar()
    print("=== DISPOSITIVOS ===\n")
    if not dispositivos_compartidos:
        print("No hay dispositivos en el sistema.")
    else:
        for i, disp in enumerate(dispositivos_compartidos, 1):
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

# ========== MENÚ ADMIN ==========

def gestionar_dispositivos():
    while True:
        limpiar()
        print("=== GESTIÓN DE DISPOSITIVOS ===")
        print("\n1. Agregar dispositivo")
        print("2. Listar dispositivos")
        print("3. Buscar dispositivo")
        print("4. Eliminar dispositivo")
        print("0. Volver")
        
        opcion = input("\nOpción: ")
        
        if opcion == "1":
            limpiar()
            nombre = input("Nombre: ").strip()
            tipo = input("Tipo: ").strip()
            disp = Dispositivo(nombre, tipo)
            usuario_actual.agregar_dispositivo(disp)
            dispositivos_compartidos.append(disp)
            print(f"\n✓ Dispositivo {nombre} agregado")
            pausar()
            
        elif opcion == "2":
            limpiar()
            print("=== DISPOSITIVOS ===\n")
            if not dispositivos_compartidos:
                print("No hay dispositivos")
            else:
                for i, d in enumerate(dispositivos_compartidos, 1):
                    print(f"{i}. {d}")
            pausar()
            
        elif opcion == "3":
            limpiar()
            nombre = input("Nombre a buscar: ").strip()
            encontrado = False
            for d in dispositivos_compartidos:
                if d.get_nombre_dispositivo().lower() == nombre.lower():
                    print(f"\n✓ Encontrado: {d}")
                    encontrado = True
                    break
            if not encontrado:
                print(f"❌ No se encontró '{nombre}'")
            pausar()
            
        elif opcion == "4":
            limpiar()
            nombre = input("Nombre a eliminar: ").strip()
            for i, d in enumerate(dispositivos_compartidos):
                if d.get_nombre_dispositivo().lower() == nombre.lower():
                    dispositivos_compartidos.pop(i)
                    if d in usuario_actual.dispositivos:
                        usuario_actual.dispositivos.remove(d)
                    print(f"\n✓ Dispositivo {nombre} eliminado")
                    pausar()
                    break
            else:
                print(f"❌ No se encontró '{nombre}'")
                pausar()
                
        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida")
            pausar()

def cambiar_rol_usuario():
    limpiar()
    print("=== CAMBIAR ROL ===\n")
    
    if len(usuarios) <= 1:
        print("No hay otros usuarios")
        pausar()
        return
    
    for i, u in enumerate(usuarios, 1):
        print(f"{i}. {u.get_nombre()} - {u.get_email()} ({u.get_rol()})")
    
    try:
        num = int(input("\nNúmero de usuario: ")) - 1
        if 0 <= num < len(usuarios):
            seleccionado = usuarios[num]
            
            if seleccionado == usuario_actual:
                print("❌ No podés cambiar tu propio rol")
            else:
                print(f"\nUsuario: {seleccionado.get_nombre()}")
                print("1. Admin")
                print("2. Usuario")
                nuevo = input("Nuevo rol: ")
                
                if nuevo == "1":
                    seleccionado.set_rol("admin")
                    print("✓ Cambiado a admin")
                elif nuevo == "2":
                    seleccionado.set_rol("usuario")
                    print("✓ Cambiado a usuario")
                else:
                    print("❌ Opción inválida")
        else:
            print("❌ Número inválido")
    except ValueError:
        print("❌ Entrada inválida")
    pausar()

def menu_admin():
    global usuario_actual
    while True:
        limpiar()
        print(f"=== MENÚ ADMIN - {usuario_actual.get_nombre()} ===")
        print("\n1. Gestionar dispositivos")
        print("2. Cambiar rol de usuario")
        print("0. Cerrar sesión")
        
        opcion = input("\nOpción: ")
        
        if opcion == "1":
            gestionar_dispositivos()
        elif opcion == "2":
            cambiar_rol_usuario()
        elif opcion == "0":
            usuario_actual = None
            break
        else:
            print("❌ Opción inválida")
            pausar()



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