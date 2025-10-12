
class Automatizacion:
    def __init__(self, descripcion, condicion=None):
        self.__descripcion = descripcion
        self.__condicion = condicion
        self.__acciones = []

    def agregar_accion(self, accion):
        self.__acciones.append(accion)
        return f"Acción {accion} agregada a la automatización."

    def ejecutar(self, dispositivos):
        resultados = []
        for accion in self.__acciones:
            for dispositivo in dispositivos:
                resultados.append(dispositivo.ejecutar_accion(accion))
        return resultados

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def get_descripcion(self):
        return self.__descripcion

    def set_condicion(self, condicion):
        self.__condicion = condicion

    def get_condicion(self):
        return self.__condicion
