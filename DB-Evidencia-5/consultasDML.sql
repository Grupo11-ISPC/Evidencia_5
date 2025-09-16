INSERT INTO usuarios (id_usuario, nombre, email) VALUES
(1, 'Ana', 'ana.garcia@email.com'),
(2, 'Luis', 'luis.perez@email.com'),
(3, 'María', 'maria.lopez@email.com'),
(4, 'Carlos', 'carlos.sanchez@email.com'),
(5, 'Sofía', 'sofia.martinez@email.com');

INSERT INTO dispositivos (nombre_dispositivo, tipo_dispositivo, estado_dispositivo, id_usuario) VALUES
('luz Sala', 'Iluminación', 1, 1),
('Termostato', 'Climatización', 0, 1),
('Enchufe Cocina', 'Energía', 1, 2),
('Sensor Puerta', 'Seguridad', 0, 2),
('Cámara Exterior', 'Seguridad', 1, 3),
('Luz Dormitorio', 'Iluminación', 0, 3),
('Aire Acondicionado', 'Climatización', 1, 4),
('Enchufe TV', 'Energía', 0, 4),
('Detector Humo', 'Seguridad', 1, 5),
('Luz Jardín', 'Iluminación', 0, 5);

INSERT INTO automatizaciones (id_automatizacion, descripcion, condicion, id_usuario) VALUES
(1, 'Encender luces al anochecer', 'hora = 20:00', 1),
(2, 'Apagar termostato si ventana abierta', 'sensor_puerta = 1', 1),
(3, 'Encender enchufe Cocina al llegar a casa', 'usuario_llega = 1', 2),
(4, 'Aviso si puerta abierta mas de 5 min', 'sensor_puerta = 1 AND tiempo > 5', 2),
(5, 'Apagar luces al salir de casa', 'usuario_sale = 1', 1),
(6, 'Activar alarma al detectar movimiento', 'sensor_movimiento = 1', 2),
(7, 'Encender calefaccion por la manana', 'hora = 07:00', 1),
(8, 'Notificar temperatura alta', 'temperatura > 30', 2);

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
('apagar', 'Luz Jardín', 5, 10),
('encender', 'Cámara Exterior', 6, 5),
('encender', 'Aire Acondicionado', 7, 7),
('notificar', 'Detector Humo', 8, 9);

-- CONSULTAS SIMPLES DE LAS TABLAS
SELECT * FROM usuarios;
SELECT * FROM dispositivos;
SELECT * FROM automatizaciones;
SELECT * FROM acciones;


