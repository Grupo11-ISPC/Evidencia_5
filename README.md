# 🏠 Smart Home Solutions - Sistema de Gestión de Hogar Inteligente

## 📘 Descripción General

**Smart Home Solutions** es un sistema integral de gestión de hogares inteligentes que permite controlar y automatizar dispositivos IoT a través de una interfaz de línea de comandos. Esta solución está diseñada para facilitar el manejo centralizado de dispositivos, la creación de automatizaciones personalizadas y la gestión de usuarios con distintos niveles de acceso.

## 🎯 Objetivo

En un contexto donde la domótica y el Internet de las Cosas (IoT) son cada vez más comunes, surge la necesidad de contar con herramientas que integren y simplifiquen el control de múltiples dispositivos inteligentes. Este proyecto busca cubrir esa necesidad mediante:

- ✅ **Gestión de dispositivos**: iluminación, climatización, seguridad y energía.
- ⚙️ **Automatizaciones inteligentes**: ejecución de acciones según condiciones definidas.
- 🔐 **Control de acceso**: usuarios con diferentes roles y permisos.
- 💾 **Persistencia de datos**: almacenamiento confiable con SQLite.

Además, esta aplicación fue desarrollada como evidencia práctica de conceptos clave como **Programación Orientada a Objetos (POO)**, **manejo de bases de datos relacionales** y el patrón de arquitectura **DAO (Data Access Object)**.

---

## 🧰 Funcionalidades Principales

### 👤 Gestión de Usuarios
- Registro con validación de datos.
- Inicio y cierre de sesión (login/logout).
- Roles de usuario: **administrador** y **usuario estándar**.
- Modificación de roles (exclusiva para administradores).
- Consulta de información personal.

### 💡 Gestión de Dispositivos
- Operaciones **CRUD** (Crear, Leer, Actualizar, Eliminar).
- Tipos de dispositivos soportados:
  - Iluminación
  - Climatización
  - Seguridad
  - Energía
- Encendido y apagado de dispositivos.
- Asignación de dispositivos a usuarios.

### 🤖 Sistema de Automatizaciones
- Creación de reglas condicionales personalizadas.
- Asociación de múltiples acciones por evento.
- Tipos de acciones disponibles:
  - Encendido/apagado de dispositivos.
  - Modificación de estados.
  - Envío de notificaciones.
  - Configuración de valores personalizados.

### 🗃️ Persistencia y Base de Datos
- Estructura relacional compuesta por 4 tablas principales:
  - `usuarios`: información personal y roles.
  - `dispositivos`: catálogo de dispositivos IoT.
  - `automatizaciones`: definición de reglas automáticas.
  - `acciones`: conjunto de operaciones asociadas a cada automatización.
- Uso de claves foráneas para mantener la integridad referencial.
- Consultas SQL optimizadas (simples, multitabla, subconsultas).

---

## 🧱 Arquitectura del Proyecto


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

## 🛠️ Tecnologías Utilizadas

- **Lenguaje**: Python 3.x  
- **Base de Datos**: SQLite 3

---

## 🚀 Posibles Mejoras Futuras

- Desarrollo de una **interfaz gráfica (GUI)** o aplicación móvil.
- Soporte para **nuevas categorías de dispositivos** inteligentes.
- Implementación de un **sistema de programación de tareas** (scheduler).
- Generación de **reportes y estadísticas de uso**.
- **Respaldos automáticos** de la base de datos.
- **Encriptación de contraseñas** mediante hashing seguro.

---

## 👥 Autores

- 📌 Victor Andrés Bianchi Núñez – `DNI: 42.258.135`  
- 📌 Federico David Udovich – `DNI: 42.383.964`  
- 📌 Federico Martín Pierrestegui – `DNI: 35.257.982`  
- 📌 Gabriel Alejandro Farias – `DNI: 36.223.373`  

---
