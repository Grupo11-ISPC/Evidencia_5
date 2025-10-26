# 🏠 Smart Home Solutions

Sistema de gestión de hogar inteligente desarrollado en Python que permite controlar dispositivos IoT, crear automatizaciones y gestionar usuarios con diferentes niveles de acceso.

## 📋 Descripción

Smart Home Solutions es una aplicación de consola que facilita el control centralizado de dispositivos domóticos como luces, termostatos, cámaras de seguridad y enchufes inteligentes. El sistema permite crear reglas de automatización y asignar roles a los usuarios.

## ✨ Características

### Gestión de Usuarios
- Registro e inicio de sesión
- Dos roles: **admin** y **usuario**
- El primer usuario registrado es administrador automáticamente
- Los administradores pueden cambiar roles de otros usuarios

### Gestión de Dispositivos
- Crear, listar, modificar y eliminar dispositivos
- Tipos: Iluminación, Climatización, Seguridad, Energía, etc
- Cambiar estado (encendido/apagado)
- Cada dispositivo se asocia a un usuario

### Automatizaciones
- Crear reglas basadas en condiciones
- Asignar múltiples acciones por automatización
- Tipos de acciones: encender, apagar, notificar, cambiar estado (pendiente de implementación)

## 🗂️ Estructura del Proyecto

```
POO-SmartHome/
├── conn/
│   └── db_conn.py              # Conexión a MySQL
├── dao/
│   ├── interfaces/
│   │   ├── i_dispositivo_dao.py
│   │   └── i_usuario_dao.py
│   ├── dispositivo_dao.py      # Operaciones CRUD dispositivos
│   └── usuario_dao.py          # Operaciones CRUD usuarios
├── dominio/
│   ├── accion.py
│   ├── automatizacion.py
│   ├── dispositivo.py
│   └── usuario.py
├── tests/                      # Pruebas unitarias
└── main.py                     # Aplicación principal

BD-Evidencia-6/
├── consultasDDL.sql           # Estructura de base de datos
└── consultasDML.sql           # Datos de ejemplo y consultas
```

## 🛠️ Tecnologías

- **Python 3.x**
- **MySQL** (base de datos)
- **mysql-connector-python** (conexión a BD)

## 🚀 Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/Grupo11-ISPC/Evidencia_5.git
cd POO-SmartHome
```

2. **Instalar dependencias**
```bash
pip install mysql-connector-python
```

3. **Configurar MySQL**
   - Crear base de datos `smart_home_solutions`
   - Ejecutar `BD-Evidencia-6/consultasDDL.sql`
   - (Opcional) Ejecutar `BD-Evidencia-6/consultasDML.sql` para datos de prueba

4. **Configurar conexión**
   - Editar `conn/db_conn.py` con tus credenciales de MySQL:
   ```python
   _HOST = 'localhost'
   _PORT = 3306
   _DATABASE = 'smart_home_solutions'
   _USER = 'tu_usuario'
   _PASSWORD = 'tu_contraseña'
   ```

5. **Ejecutar la aplicación**
```bash
python main.py
```

## 📊 Base de Datos

La base de datos consta de 4 tablas principales:

- **usuarios**: id, nombre, email, password, rol, fecha_creacion
- **dispositivos**: id, nombre_dispositivo, tipo_dispositivo, estado_dispositivo, id_usuario, fecha_creacion
- **automatizacion**: id, descripcion, condicion, id_usuario, fecha_creacion
- **acciones**: id, tipo_accion, valor_configurado, id_automatizacion, fecha_creacion

Todas las tablas utilizan claves foráneas con `ON DELETE CASCADE` para mantener la integridad referencial.

## Uso

### Primer inicio
1. Registrar el primer usuario (será administrador)
2. Iniciar sesión con las credenciales creadas

### Menú Administrador
- Gestionar dispositivos (crear, listar, modificar, eliminar)
- Cambiar roles de usuarios

### Menú Usuario
- Consultar datos personales
- Ver lista de dispositivos del sistema

## Tests

Ejecutar las pruebas unitarias:
```bash
pytest tests/
```

Los tests cubren:
- Creación y validación de usuarios
- Operaciones con dispositivos
- Funcionalidad de automatizaciones y acciones

## 👥 Autores

- Victor Andrés Bianchi Núñez – DNI: 42.258.135
- Federico David Udovich – DNI: 42.383.964
- Federico Martín Pierrestegui – DNI: 35.257.982
- Gabriel Alejandro Farias – DNI: 36.223.373

## 📝 Notas

- El sistema usa MySQL
- Se requiere tener MySQL instalado y corriendo

## 🔮 Mejoras Futuras

- Encriptación de contraseñas
- Interfaz gráfica (GUI)
- Soporte para más tipos de dispositivos
- Sistema de notificaciones en tiempo real