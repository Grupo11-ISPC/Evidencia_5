from src.dominio.accion import Accion

def test_creacion_accion():
    accion = Accion("Encender", 5)
    assert accion.tipo_accion == "Encender"
    assert accion.valor_configurado == 5

def test_str():
    accion = Accion("Apagar", 0)
    assert str(accion) == "Accion: Apagar, Valor Configurado: 0"

def test_getters_setters():
    accion = Accion("Encender", 10)
    accion.set_tipo_accion("Apagar")
    accion.set_valor_configurado(20)
    assert accion.get_tipo_accion() == "Apagar"
    assert accion.get_valor_configurado() == 20

def test_realizar_accion():
    accion = Accion("Encender", 15)
    resultado = accion.realizar_accion()
    assert resultado == "Realizando acción: Encender con valor: 15"
