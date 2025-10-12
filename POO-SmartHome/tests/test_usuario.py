from dominio.usuario import Usuario
from dominio.dispositivo import Dispositivo
from dominio.automatizacion import Automatizacion
from dominio.accion import Accion

def test_creacion_usuario():
    u = Usuario("Juan", "juan@gmail.com", "123456", "admin")
    assert u.nombre == "Juan"
    assert u.password == "123456"
    assert u.email == "juan@gmail.com"
    assert u.rol == "admin"

def test_agregar_dispositivo():
    u = Usuario("Ana", "ana@gmail.com", "654321", "user")
    d = Dispositivo("Luz", "Apagado")
    u.agregar_dispositivo(d)
    assert d in u.dispositivos

def test_eliminar_dispositivo():
    u = Usuario("Ana", "ana@gmail.com", "654321", "user")
    d = Dispositivo("Luz", "Apagado")
    u.agregar_dispositivo(d)
    u.eliminar_dispositivo(d)
    assert d not in u.dispositivos