-- ========== INSERT ==========

-- Insertar usuarios
INSERT INTO usuarios (nombre, email, password, rol) VALUES
('Ana', 'ana.garcia@email.com', '$2y$10$abcdefghijk', 'admin'),
('Luis', 'luis.perez@email.com', '$2y$10$lmnopqrstuv', 'usuario'),
('Maria', 'maria.lopez@email.com', '$2y$10$wxyzabcdefg', 'usuario'),
('Carlos', 'carlos.sanchez@email.com', '$2y$10$hijklmnopqr', 'usuario'),
('Sofia', 'sofia.martinez@email.com', '$2y$10$stuvwxyzabc', 'usuario'),
('Federico', 'federico@email.com', '$2y$10$defghijklmn', 'usuario'),
('Andres', 'andres@email.com', '$2y$10$opqrstuvwxy', 'usuario'),
('Gabriel', 'gabriel@email.com', '$2y$10$zabcdefghij', 'usuario');


-- Insertar dispositivos
INSERT INTO dispositivos (nombre_dispositivo, tipo_dispositivo, estado_dispositivo, id_usuario) VALUES
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

-- Insertar automatizaciones
INSERT INTO automatizacion (descripcion, condicion, id_usuario) VALUES
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

-- Insertar acciones 
INSERT INTO acciones (tipo_accion, valor_configurado, id_automatizacion) VALUES
('encender', 'dispositivo_id=1', 1),
('cambiar_estado', 'dispositivo_id=2', 1),
('apagar', 'dispositivo_id=3', 2),
('notificar', 'dispositivo_id=4', 2),
('encender', 'dispositivo_id=6', 1),
('apagar', 'dispositivo_id=2', 2),
('encender', 'dispositivo_id=3', 3),
('notificar', 'dispositivo_id=4', 4),
('apagar', 'dispositivo_id=1', 5),
('apagar', 'dispositivo_id=10', 5),
('encender', 'dispositivo_id=5', 6),
('encender', 'dispositivo_id=7', 7),
('notificar', 'dispositivo_id=9', 8),
('encender', 'dispositivo_id=12', 9),
('apagar', 'dispositivo_id=13', 10),
('encender', 'dispositivo_id=14', 11),
('notificar', 'dispositivo_id=11', 12);


-- ========== CONSULTAS SIMPLES ==========
SELECT * FROM usuarios;
SELECT * FROM dispositivos;
SELECT * FROM automatizacion;
SELECT * FROM acciones;


-- ========== CONSULTAS MULTITABLA ==========

/* Esta consulta trae el nombre del dispositivo y el tipo, de los usuarios */
SELECT u.nombre AS usuario, d.nombre_dispositivo, d.tipo_dispositivo
FROM dispositivos d
INNER JOIN usuarios u ON d.id_usuario = u.id;

/* Esta consulta trae la descripcion y la condicion de las automatizaciones que tiene cada usuario */
SELECT u.nombre AS usuario, a.descripcion, a.condicion
FROM automatizacion a
INNER JOIN usuarios u ON a.id_usuario = u.id;

/* Esta consulta nos trae las acciones y los dispositivos que participan en la automatizacion*/

SELECT a.descripcion AS automatizacion, ac.tipo_accion, ac.valor_configurado
FROM acciones ac
INNER JOIN automatizacion a ON ac.id_automatizacion = a.id;

/* Esta consulta trae los usuarios con los nombres de dispositivos y automatizaciones que tengan asociados */
SELECT u.nombre AS usuario, d.nombre_dispositivo, a.descripcion AS automatizacion
FROM usuarios u
LEFT JOIN dispositivos d ON u.id = d.id_usuario
LEFT JOIN automatizacion a ON u.id = a.id_usuario
ORDER BY u.id;


-- ========== SUBCONSULTAS ==========

/* Esta subconsulta muestra los nombres de los usuarios que tienen al menos un dispositivo de tipo seguridad */
SELECT nombre 
FROM usuarios 
WHERE id IN (
    SELECT DISTINCT id_usuario 
    FROM dispositivos 
    WHERE tipo_dispositivo = 'Seguridad'
);

/* Esta subconsulta nos trae la descripcion de las automatizaciones vinculadas a dispositivos encendidos*/
SELECT descripcion
FROM automatizacion
WHERE id IN (
    SELECT DISTINCT id_automatizacion
    FROM acciones
);