class Dispositivo:
    def __init__(self, nombre_dispositivo, tipo_dispositivo, estado_dispositivo = False, id = None):
        self._id = id
        self._nombre_dispositivo = nombre_dispositivo
        self._tipo_dispositivo = tipo_dispositivo
        self._estado_dispositivo = estado_dispositivo
 
    def get_id(self):
        return self._id
    
    def set_nombre_dispositivo(self, nombre_dispositivo):
        self._nombre_dispositivo = nombre_dispositivo

    def get_nombre_dispositivo(self):
        return self._nombre_dispositivo
    
    def set_tipo_dipositivo(self, tipo_dispositivo):
        self._tipo_dispositivo= tipo_dispositivo
    
    def get_tipo_dispositivo(self):
        return self._tipo_dispositivo
    
    def set_estado_dispositivo(self, estado_dispositivo):
        self._estado_dispositivo = estado_dispositivo
    
    def get_estado_dispositivo(self):
        return self._estado_dispositivo
 
    def __str__(self):
        estado = "Encendido" if self._estado_dispositivo else "Apagado"
        return f"Dispositivo(ID: {self._id}, Nombre: {self._nombre_dispositivo}, Tipo: {self._tipo_dispositivo}, Estado: {estado})"