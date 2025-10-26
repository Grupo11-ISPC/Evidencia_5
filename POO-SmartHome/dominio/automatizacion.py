
class Automatizacion:
    def __init__(self, descripcion, condicion=None):
        self._descripcion = descripcion
        self._condicion = condicion
        self._acciones = []

    def agregar_accion(self, accion):
        self._acciones.append(accion)
        return f"Acción {accion} agregada a la automatización."

    def ejecutar(self, dispositivos):
        resultados = []
        for accion in self._acciones:
            for dispositivo in dispositivos:
                resultados.append(dispositivo.ejecutar_accion(accion))
        return resultados

    def set_descripcion(self, descripcion):
        self._descripcion = descripcion

    def get_descripcion(self):
        return self._descripcion

    def set_condicion(self, condicion):
        self._condicion = condicion

    def get_condicion(self):
        return self._condicion
