
class Automatizacion:
    def __init__(self, descripcion, condicion=None):
        self.descripcion = descripcion
        self.condicion = condicion
        self.acciones = []

    def agregar_accion(self, accion):
        self.acciones.append(accion)
        return f"Acción {accion} agregada a la automatización."

    def ejecutar(self, dispositivos):
        resultados = []
        for accion in self.acciones:
            for dispositivo in dispositivos:
                resultados.append(dispositivo.ejecutar_accion(accion))
        return resultados

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_descripcion(self):
        return self.descripcion

    def set_condicion(self, condicion):
        self.condicion = condicion

    def get_condicion(self):
        return self.condicion
