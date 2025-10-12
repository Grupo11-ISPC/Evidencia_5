from dominio.dispositivo import Dispositivo

def test_creacion_dispositivo():
    d = Dispositivo("Luz", "Apagado")
    assert d.nombre_dispositivo == "Luz"
    assert d.get_estado() == "Apagado"

def test_str():
    d = Dispositivo("Sensor", "iluminacion", True)
    assert str(d) == "Dispositivo: Sensor, Tipo: iluminacion, Estado: Encendido"


def test_getters_setters():
    d = Dispositivo("Luz", "Apagado")
    d.set_nombre_dispositivo("Ventilador")
    d.set_estado("Encendido")
    assert d.get_nombre_dispositivo() == "Ventilador"
    assert d.get_estado() == "Encendido"
