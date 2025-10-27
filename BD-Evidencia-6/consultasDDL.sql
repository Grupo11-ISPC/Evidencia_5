

CREATE TABLE usuarios(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    rol ENUM('admin', 'user') DEFAULT 'user'
);

CREATE TABLE dispositivos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    tipo VARCHAR(50),
    estado TINYINT DEFAULT 0,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE
);

CREATE TABLE automatizaciones (
    id INT PRIMARY KEY AUTO_INCREMENT,
    descripcion VARCHAR(255),
    condicion VARCHAR(255),
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE
);

CREATE TABLE acciones (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tipo VARCHAR(50),
    valor_configurado VARCHAR(255),
    id_automatizacion INT,
    id_dispositivo INT,
    FOREIGN KEY (id_automatizacion) REFERENCES automatizaciones(id) ON DELETE CASCADE,
    FOREIGN KEY (id_dispositivo) REFERENCES dispositivos(id) ON DELETE CASCADE
);