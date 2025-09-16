INSERT INTO usuarios (id_usuario, nombre, email) VALUES
(1, 'Ana', 'ana.garcia@email.com'),
(2, 'Luis', 'luis.perez@email.com');

INSERT INTO dispositivos (nombre_dispositivo, tipo_dispositivo, estado_dispositivo, id_usuario) VALUES
('luz Sala', 'Iluminación', 1, 1),
('Termostato', 'Climatización', 0, 1),
('Enchufe Cocina', 'Energía', 1, 2),
('Sensor Puerta', 'Seguridad', 0, 2);
