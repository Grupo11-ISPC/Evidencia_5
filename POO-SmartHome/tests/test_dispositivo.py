from src.dispositivo import Dispositivo

def test_creacion_dispositivo():
    d = Dispositivo("Luz", "Apagado")
    assert d.nombre == "Luz"
    assert d.estado == "Apagado"

def test_str():
    d = Dispositivo("Sensor", "Encendido")
    assert str(d) == "Dispositivo: Sensor, Estado: Encendido"

def test_getters_setters():
    d = Dispositivo("Luz", "Apagado")
    d.set_nombre("Ventilador")
    d.set_estado("Encendido")
    assert d.get_nombre() == "Ventilador"
    assert d.get_estado() == "Encendido"
