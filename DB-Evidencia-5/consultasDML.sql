INSERT INTO usuarios (id_usuario, nombre, email) VALUES
(1, 'Ana', 'ana.garcia@email.com'),
(2, 'Luis', 'luis.perez@email.com');

INSERT INTO dispositivos (nombre_dispositivo, tipo_dispositivo, estado_dispositivo, id_usuario) VALUES
('luz Sala', 'Iluminación', 1, 1),
('Termostato', 'Climatización', 0, 1),
('Enchufe Cocina', 'Energía', 1, 2),
('Sensor Puerta', 'Seguridad', 0, 2);

INSERT INTO automatizaciones (id_automatizacion, descripcion, condicion, id_usuario) VALUES
(1, 'Encender luces al anochecer', 'hora = 20:00', 1),
(2, 'Apagar termostato si ventana abierta', 'sensor_puerta = 1', 1),
(3, 'Encender enchufe Cocina al llegar a casa', 'usuario_llega = 1', 2),
(4, 'Aviso si puerta abierta más de 5 min', 'sensor_puerta = 1 AND tiempo > 5', 2),
(5, 'Apagar luces al salir de casa', 'usuario_sale = 1', 1),
(6, 'Activar alarma al detectar movimiento', 'sensor_movimiento = 1', 2),
(7, 'Encender calefacción por la mañana', 'hora = 07:00', 1),
(8, 'Notificar temperatura alta', 'temperatura > 30', 2);

