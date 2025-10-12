from dominio.automatizacion import Automatizacion
from dominio.dispositivo import Dispositivo
from dominio.accion import Accion

def test_automatizacion_con_dispositivos():
    auto = Automatizacion("Prueba de automatización")
    auto.agregar_accion(Accion("encender", None))
    auto.agregar_accion(Accion("set_nombre", "Lámpara nueva"))

    d1 = Dispositivo("Luz", "iluminacion")
    d2 = Dispositivo("Ventilador", "clima")

    resultados = auto.ejecutar([d1, d2])

    # Debe haber 2 acciones * 2 dispositivos = 4 resultados
    assert len(resultados) == 4

    resultado_esperado = [
    "El dispositivo Luz ha sido encendido.",
    "El dispositivo Ventilador ha sido encendido.",
    "El dispositivo ahora se llama Lámpara nueva.",
    "El dispositivo ahora se llama Lámpara nueva."
]
    assert resultados == resultado_esperado


