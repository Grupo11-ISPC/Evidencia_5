INSERT INTO usuarios (id_usuario, nombre, email) VALUES
(1, 'Ana', 'ana.garcia@email.com'),
(2, 'Luis', 'luis.perez@email.com'),
(3, 'Maria', 'maria.lopez@email.com'),
(4, 'Carlos', 'carlos.sanchez@email.com'),
(5, 'Sofia', 'sofia.martinez@email.com'),
(6, 'Federico', 'federico@email.com'),
(7, 'Andres', 'andres@email.com'),
(8,'Gabriel', 'gabriel@email.com');


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

INSERT INTO automatizaciones (id_automatizacion, descripcion, condicion, id_usuario) VALUES
(1, 'Encender luces al anochecer', 'hora = 20:00', 1),
(2, 'Apagar termostato si ventana abierta', 'sensor_puerta = 1', 1),
(3, 'Encender enchufe Cocina al llegar a casa', 'usuario_llega = 1', 2),
(4, 'Aviso si puerta abierta mas de 5 min', 'sensor_puerta = 1 AND tiempo > 5', 2),
(5, 'Apagar luces al salir de casa', 'usuario_sale = 1', 1),
(6, 'Activar alarma al detectar movimiento', 'sensor_movimiento = 1', 2),
(7, 'Encender calefaccion por la manana', 'hora = 07:00', 1),
(8, 'Notificar temperatura alta', 'temperatura > 30', 2),
(9, 'Encender luces del balcon al anochecer', 'hora = 20:00', 7),
(10, 'Apagar enchufe PC al salir de casa', 'usuario_sale = 1', 8),
(11, 'Activar camara interior si no hay movimiento por 10 min', 'sensor_movimiento = 0 AND tiempo > 10', 7),
(12, 'Notificar movimiento detectado en sala', 'sensor_movimiento = 1', 6);

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
('notificar', 'Detector Humo', 8, 9),
('encender', 'Luz Balcon', 9, 12),
('apagar', 'Enchufe PC', 10, 13),
('encender', 'Camara Interior', 11, 14),
('notificar', 'Sensor Movimiento Sala', 12, 11);

-- CONSULTAS SIMPLES DE LAS TABLAS
SELECT * FROM usuarios;
SELECT * FROM dispositivos;
SELECT * FROM automatizaciones;
SELECT * FROM acciones;

-- CONSULTAS MULTITABLA--   

/*esta consulta trae el nombre del dispositivo y el tipo, de los usuarios */
SELECT u.nombre AS usuario, d.nombre_dispositivo, d.tipo_dispositivo
FROM dispositivos d
INNER JOIN usuarios u ON d.id_usuario = u.id_usuario;

/* esta consulta trae la descripcion y la condicion de las automatizaciones que tiene cada usuario*/
SELECT u.nombre AS usuario, a.descripcion, a.condicion
FROM automatizaciones a
INNER JOIN usuarios u ON a.id_usuario = u.id_usuario;

/* esta consulta nos trae las acciones y los dispostivos que participan en la automatizacion*/
SELECT a.descripcion AS automatizacion, ac.tipo_accion, d.nombre_dispositivo
FROM acciones ac
INNER JOIN automatizaciones a ON ac.id_automatizacion = a.id_automatizacion
INNER JOIN dispositivos d ON ac.id_dispositivo = d.id_dispositivo;

/* esta consulta trae los usuarios con los nombres de dispositivos y automatizaciones que tengan asociados.*/
SELECT u.nombre AS usuario, d.nombre_dispositivo, a.descripcion AS automatizacion
FROM usuarios u
LEFT JOIN dispositivos d ON u.id_usuario = d.id_usuario
LEFT JOIN automatizaciones a ON u.id_usuario = a.id_usuario
ORDER BY u.id_usuario;

-- SUBCONSULTAS--

/* esta subconsulta muestra los nombres de los usuarios que tienen al menos un dispositivo de tipo seguridad.*/
SELECT nombre 
FROM usuarios 
WHERE id_usuario IN (
    SELECT DISTINCT id_usuario 
    FROM dispositivos 
    WHERE tipo_dispositivo = 'Seguridad'
);

/* esta subconsulta nos trae la descripcion de las automatizaciones que actualmente estan encendidas*/
SELECT descripcion
FROM automatizaciones
WHERE id_automatizacion IN (
    SELECT id_automatizacion
    FROM acciones
    WHERE id_dispositivo IN (
        SELECT id_dispositivo
        FROM dispositivos
        WHERE estado_dispositivo = 1
    )
);




