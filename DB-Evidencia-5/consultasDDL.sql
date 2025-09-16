CREATE DATABASE smart_home_solutions;
USE smart_home_solutions;

CREATE TABLE usuarios(
	id_usuario INT PRIMARY KEY NOT NULL,
	nombre VARCHAR(50),
	email VARCHAR (50)
);

CREATE TABLE dispositivos(
	id_dispositivo INT PRIMARY KEY,
	nombre_dispositivo VARCHAR(50),
	tipo_dispositivo VARCHAR(50),
	estado_dispositivo BIT,
	id_usuario INT,
	FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

CREATE TABLE automatizaciones (
    id_automatizacion INT PRIMARY KEY,
    descripcion VARCHAR(50),
    condicion VARCHAR(50),
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);
