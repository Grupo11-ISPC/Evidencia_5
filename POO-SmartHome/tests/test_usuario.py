import pytest
from dominio.usuario import Usuario
from dominio.dispositivo import Dispositivo
from dominio.automatizacion import Automatizacion
from dominio.accion import Accion

def test_creacion_usuario():
    u = Usuario("Juan", "juan@gmail.com", "123456", "admin")
    assert u.get_nombre() == "Juan"
    assert u.get_email() == "juan@gmail.com"
    assert u.get_rol() == "admin"


def test_agregar_dispositivo():
    u = Usuario("Ana", "ana@gmail.com", "123456", "user")
    d = Dispositivo("Luz", "Apagado")

    resultado = u.agregar_dispositivo(d)

    assert "Dispositivo Luz agregado." == resultado
    assert "Luz" in u.listar_dispositivos()


def test_eliminar_dispositivo():
    u = Usuario("Ana", "ana@gmail.com", "123456", "user")
    d = Dispositivo("Luz", "Apagado")

    u.agregar_dispositivo(d)
    resultado = u.eliminar_dispositivo(d)

    assert resultado == "Dispositivo Luz eliminado."
    assert "Luz" not in u.listar_dispositivos()


def test_agregar_automatizacion():
    u = Usuario("Carlos", "carlos@gmail.com", "abcdef", "admin")
    a = Automatizacion("Encender luces")

    resultado = u.agregar_automatizacion(a)

    assert resultado == "Automatización Encender luces agregada."
    assert "Encender luces" in u.listar_automatizaciones()

def test_ejecutar_accion_en_dispositivo():
    u = Usuario("Ana", "ana@gmail.com", "123456", "user")
    d = Dispositivo("Luz", "iluminacion") 
    u.agregar_dispositivo(d)
    resultado = u.ejecutar_accion_en_dispositivo("Luz", Accion("encender", None))
   
    assert resultado == "El dispositivo Luz ha sido encendido."
    assert d.get_estado() == "Encendido"


def test_validar_usuario_invalido():
    with pytest.raises(ValueError):
        Usuario("", "correo_invalido", "123", "desconocido")