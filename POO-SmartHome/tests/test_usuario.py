from src.usuario import Usuario
from src.dispositivo import Dispositivo
from src.automatizacion import Automatizacion
from src.accion import Accion

def test_creacion_usuario():
    u = Usuario("Juan", "1234")
    assert u.nombre == "Juan"
    assert u._contrasena == "1234"

def test_agregar_dispositivo():
    u = Usuario("Ana", "abcd")
    d = Dispositivo("Luz", "Apagado")
    u.agregar_dispositivo(d)
    assert d in u.dispositivos

def test_eliminar_dispositivo():
    u = Usuario("Ana", "abcd")
    d = Dispositivo("Luz", "Apagado")
    u.agregar_dispositivo(d)
    u.eliminar_dispositivo(d)
    assert d not in u.dispositivos