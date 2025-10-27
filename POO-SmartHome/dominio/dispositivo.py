class Dispositivo:
    def __init__(self, nombre, tipo, estado = False, id = None):
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
        self.__estado = estado
 
    def get_id(self):
        return self.__id
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre
    
    def set_tipo(self, tipo):
        self.__tipo= tipo
    
    def get_tipo(self):
        return self.__tipo
    
    def set_estado(self, estado):
        self.__estado = estado
    
    def get_estado(self):
        return self.__estado
 
    def __str__(self):
        estado = "Encendido" if self.__estado else "Apagado"
        return f"Dispositivo(ID: {self.__id}, Nombre: {self.__nombre}, Tipo: {self.__tipo}, Estado: {estado})"