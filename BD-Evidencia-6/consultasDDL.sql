-- CREATE DATABASE smart_home_solutions;
-- USE smart_home_solutions;

CREATE TABLE usuarios(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    rol ENUM('admin', 'usuario') DEFAULT 'usuario',
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE dispositivos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_dispositivo VARCHAR(100),
    tipo_dispositivo VARCHAR(50),
    estado_dispositivo TINYINT(1) DEFAULT 0,
    id_usuario INT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE
);

CREATE TABLE automatizacion (
    id INT PRIMARY KEY AUTO_INCREMENT,
    descripcion VARCHAR(255),
    condicion TEXT,
    id_usuario INT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE
);

CREATE TABLE acciones (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tipo_accion VARCHAR(50),
    valor_configurado VARCHAR(255),
    id_automatizacion INT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_automatizacion) REFERENCES automatizacion(id) ON DELETE CASCADE
);