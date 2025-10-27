INSERT INTO usuarios (nombre, email, password, rol) VALUES
('Ana', 'ana.garcia@email.com', '$2y$10$abcdefghijk', 'admin'),
('Luis', 'luis.perez@email.com', '$2y$10$lmnopqrstuv', 'user'),
('Maria', 'maria.lopez@email.com', '$2y$10$wxyzabcdefg', 'user'),
('Carlos', 'carlos.sanchez@email.com', '$2y$10$hijklmnopqr', 'user'),
('Sofia', 'sofia.martinez@email.com', '$2y$10$stuvwxyzabc', 'user'),
('Federico', 'federico@email.com', '$2y$10$defghijklmn', 'user'),
('Andres', 'andres@email.com', '$2y$10$opqrstuvwxy', 'user'),
('Gabriel', 'gabriel@email.com', '$2y$10$zabcdefghij', 'user');

INSERT INTO dispositivos (nombre, tipo, estado, id_usuario) VALUES
('luz Sala', 'Iluminacion', 1, 1),
('Termostato', 'Climatizacion', 0, 1),
('Enchufe Cocina', 'Energia', 1, 2),
('Sensor Puerta', 'Seguridad', 0, 2),
('Camara Exterior', 'Seguridad', 1, 3),
('Luz Dormitorio', 'Iluminacion', 0, 3),
('Aire Acondicionado', 'Climatizacion', 1, 4),
('Enchufe TV', 'Energia', 0, 4),
('Detector Humo', 'Seguridad', 1, 5),
('Luz Jardin', 'Iluminacion', 0, 5),
('Sensor Movimiento Sala', 'Seguridad', 1, 6),
('Luz Balcon', 'Iluminacion', 0, 7),
('Enchufe PC', 'Energia', 1, 8),
('Camara Interior', 'Seguridad', 0, 6);

INSERT INTO automatizaciones (descripcion, condicion, id_usuario) VALUES
('Encender luces al anochecer', 'hora = 20:00', 1),
('Apagar termostato si ventana abierta', 'sensor_puerta = 1', 1),
('Encender enchufe Cocina al llegar a casa', 'usuario_llega = 1', 2),
('Aviso si puerta abierta mas de 5 min', 'sensor_puerta = 1 AND tiempo > 5', 2),
('Apagar luces al salir de casa', 'usuario_sale = 1', 1),
('Activar alarma al detectar movimiento', 'sensor_movimiento = 1', 2),
('Encender calefaccion por la manana', 'hora = 07:00', 1),
('Notificar temperatura alta', 'temperatura > 30', 2),
('Encender luces del balcon al anochecer', 'hora = 20:00', 7),
('Apagar enchufe PC al salir de casa', 'usuario_sale = 1', 8),
('Activar camara interior si no hay movimiento por 10 min', 'sensor_movimiento = 0 AND tiempo > 10', 7),
('Notificar movimiento detectado en sala', 'sensor_movimiento = 1', 6);

INSERT INTO acciones (tipo_accion, valor_configurado, id_automatizacion, id_dispositivo) VALUES
('encender', 'Luz Sala', 1, 1),
('cambiar_estado', 'Termostato', 1, 2),
('apagar', 'Enchufe Cocina', 2, 3),
('notificar', 'Sensor Puerta', 2, 4),
('encender', 'Luz Dormitorio', 1, 6),
('apagar', 'Termostato', 2, 2),
('encender', 'Enchufe Cocina', 3, 3),
('notificar', 'Sensor Puerta', 4, 4),
('apagar', 'Luz Sala', 5, 1),
('apagar', 'Luz Jardin', 5, 10),
('encender', 'Camara Exterior', 6, 5),
('encender', 'Aire Acondicionado', 7, 7),
('notificar', 'Detector Humo', 8, 9);

-- fetch 
-- CONSULTAS SIMPLES DE LAS TABLAS
SELECT * FROM usuarios;
SELECT * FROM dispositivos;
SELECT * FROM automatizaciones;
SELECT * FROM acciones;

-- CONSULTAS MULTITABLA--   

/*esta consulta trae el nombre del dispositivo y el tipo, de los usuarios */
SELECT u.nombre AS usuario, d.nombre, d.tipo
FROM dispositivos d
INNER JOIN usuarios u ON d.id_usuario = u.id;

/* esta consulta trae la descripcion y la condicion de las automatizaciones que tiene cada usuario*/
SELECT u.nombre AS usuario, a.descripcion, a.condicion
FROM automatizaciones a
INNER JOIN usuarios u ON a.id_usuario = u.id;

/* esta consulta nos trae las acciones y los dispostivos que participan en la automatizacion*/
SELECT a.descripcion AS automatizacion, ac.tipo_accion, d.nombre
FROM acciones ac
INNER JOIN automatizaciones a ON ac.id_automatizacion = a.id
INNER JOIN dispositivos d ON ac.id_dispositivo = d.id;

/* esta consulta trae los usuarios con los nombres de dispositivos y automatizaciones que tengan asociados.*/
SELECT u.nombre AS usuario, d.nombre, a.descripcion AS automatizacion
FROM usuarios u
LEFT JOIN dispositivos d ON u.id = d.id_usuario
LEFT JOIN automatizaciones a ON u.id = a.id_usuario
ORDER BY u.id;

-- SUBCONSULTAS--

/* esta subconsulta muestra los nombres de los usuarios que tienen al menos un dispositivo de tipo seguridad.*/
SELECT 
    u.nombre AS usuario, 
    d.nombre
FROM usuarios u
INNER JOIN dispositivos d ON u.id = d.id_usuario
WHERE d.tipo = 'Seguridad';

/* esta subconsulta nos trae la descripcion de las automatizaciones que actualmente estan encendidas*/
SELECT descripcion FROM automatizaciones WHERE id IN (
    SELECT id_automatizacion
    FROM acciones
    WHERE id_dispositivo IN (
        SELECT id
        FROM dispositivos
        WHERE estado = 1
    )
);