# Smart Home Solutions - Sistema de Gestión de Hogar Inteligente

## 📋 Propósito

Este proyecto consiste en un sistema integral de gestión de hogar inteligente que permite a los usuarios controlar y automatizar dispositivos domésticos a través de una interfaz de línea de comandos. El sistema está diseñado para facilitar la administración de dispositivos IoT, crear automatizaciones personalizadas y gestionar usuarios con diferentes niveles de permisos.

## 🎯 Contexto

En la era de la domótica y el Internet de las Cosas (IoT), existe una creciente necesidad de sistemas que permitan gestionar de manera eficiente múltiples dispositivos inteligentes en el hogar. Este proyecto surge como respuesta a esa necesidad, ofreciendo una solución completa que integra:

- **Gestión de dispositivos**: Control de iluminación, climatización, seguridad y energía
- **Automatizaciones inteligentes**: Programación de acciones basadas en condiciones específicas
- **Control de acceso**: Sistema de usuarios con roles diferenciados (administrador/usuario)
- **Persistencia de datos**: Base de datos SQLite para almacenamiento confiable

El proyecto se desarrolló como evidencia práctica de conceptos de POO, BD y patrón de arqutectura DAO.

## 🔧 Alcance

### Funcionalidades Implementadas

#### **Gestión de Usuarios**
- Registro de nuevos usuarios con validación de datos
- Sistema de autenticación (login/logout)
- Dos roles de usuario: administrador y usuario estándar
- Modificación de roles (solo por administradores)
- Consulta de datos personales

#### **Gestión de Dispositivos**
- CRUD completo (Crear, Leer, Actualizar, Eliminar) de dispositivos
- Tipos de dispositivos soportados:
  - Iluminación
  - Climatización
  - Seguridad
  - Energía
- Control de estado (encendido/apagado)
- Asignación de dispositivos a usuarios

#### **Sistema de Automatizaciones**
- Creación de automatizaciones con condiciones personalizadas
- Asociación de acciones a dispositivos
- Ejecución de múltiples acciones en secuencia
- Tipos de acciones disponibles:
  - Encender/Apagar dispositivos
  - Cambiar estado
  - Notificaciones
  - Configuración de valores

#### **Base de Datos**
- Modelo relacional con 4 tablas principales:
  - `usuarios`: Información de usuarios del sistema
  - `dispositivos`: Catálogo de dispositivos IoT
  - `automatizaciones`: Reglas de automatización
  - `acciones`: Acciones vinculadas a automatizaciones
- Integridad referencial mediante claves foráneas
- Consultas SQL optimizadas (simples, multitabla y subconsultas)

### Arquitectura del Proyecto

```
POO-SmartHome/
├── conn/
│   └── db_conn.py          # Conexión a base de datos
├── dao/                     # Capa de acceso a datos
│   ├── interfaces/
│   │   ├── i_dispositivo_dao.py
│   │   └── i_usuario_dao.py
│   ├── dispositivo_dao.py
│   └── usuario_dao.py
├── dominio/                 # Modelos de dominio
│   ├── accion.py
│   ├── automatizacion.py
│   ├── dispositivo.py
│   └── usuario.py
├── tests/                   # Pruebas unitarias
│   ├── test_accion.py
│   ├── test_automatizacion.py
│   ├── test_dispositivo.py
│   └── test_usuario.py
└── main.py                  # Punto de entrada de la aplicación

BD-Evidencia-6/             # Scripts SQL adicionales
├── consultasDDL.sql        # Definición de estructura
└── consultasDML.sql        # Datos de prueba y consultas
```

### Tecnologías Utilizadas

- **Lenguaje**: Python 3.x
- **Base de datos**: SQLite 3

**Posibles mejoras futuras:**
- Implementación de una interfaz web o móvil
- Soporte para más tipos de dispositivos
- Sistema de horarios avanzado (scheduler)
- Reportes y estadísticas de uso
- Respaldos automáticos de la base de datos
- Encriptación de contraseñas con hashing

## 👥 Autores
•	42258135 Victor Andrés Bianchi Núñez 
•	42383964 Federico David Udovich 
•	35257982 Federico Martin Pierrestegui 
•	36223373 Gabriel Alejandro Farias 
---