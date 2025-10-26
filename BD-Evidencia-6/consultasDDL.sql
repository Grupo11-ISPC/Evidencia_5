CREATE DATABASE smart_home_solutions;
USE smart_home_solutions;

CREATE TABLE usuarios(
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    rol ENUM('admin', 'usuario') DEFAULT 'usuario'
);

CREATE TABLE dispositivos(
    id_dispositivo INT PRIMARY KEY AUTO_INCREMENT,
    nombre_dispositivo VARCHAR(100),
    tipo_dispositivo VARCHAR(50),
    estado_dispositivo TINYINT DEFAULT 0,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

CREATE TABLE automatizaciones (
    id_automatizacion INT PRIMARY KEY AUTO_INCREMENT,
    descripcion VARCHAR(255),
    condicion VARCHAR(255),
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

CREATE TABLE acciones (
    id_accion INT PRIMARY KEY AUTO_INCREMENT,
    tipo_accion VARCHAR(50),
    valor_configurado VARCHAR(255),
    id_automatizacion INT,
    id_dispositivo INT,
    FOREIGN KEY (id_automatizacion) REFERENCES automatizaciones(id_automatizacion) ON DELETE CASCADE,
    FOREIGN KEY (id_dispositivo) REFERENCES dispositivos(id_dispositivo) ON DELETE CASCADE
);