from .accion import Accion

class Dispositivo:
    def __init__(self, nombre_dispositivo, tipo_dispositivo, estado_dispositivo = False,id = None):
        self.__id = id
        self.__nombre_dispositivo = nombre_dispositivo
        self.__tipo_dispositivo = tipo_dispositivo
        self.__estado_dispositivo = estado_dispositivo

    #Acciones
    def ejecutar_accion(self, accion):
        if accion.get_tipo_accion() == "encender":
            self.encender()
            return f"El dispositivo {self.__nombre_dispositivo} ha sido encendido."
        
        elif accion.get_tipo_accion() == "apagar":
            self.apagar()
            return f"El dispositivo {self.__nombre_dispositivo} ha sido apagado."
        
        elif accion.get_tipo_accion() == "cambiar_estado":
            self.cambiar_estado()
            return f"El dispositivo {self.__nombre_dispositivo} ha cambiado su estado."
        
        elif accion.get_tipo_accion() == "set_nombre":
            self.set_nombre_dispositivo(accion.get_valor_configurado())
            return f"El dispositivo ahora se llama {self.__nombre_dispositivo}."
        
        elif accion.get_tipo_accion() == "set_tipo":
            self.set_tipo(accion.get_valor_configurado())
            return f"El dispositivo ahora es de tipo {self.__tipo_dispositivo}."
        
        elif accion.get_tipo_accion() == "set_estado":
            self.set_estado(accion.get_valor_configurado())
            return f"El estado del dispositivo se configuró como {self.__estado_dispositivo}."
        
        else:
            return "Acción no reconocida."

   
    def encender(self):
        self.__estado_dispositivo = True
    
    def apagar(self):
        self.__estado_dispositivo = False

    def cambiar_estado(self):
        if self.__estado_dispositivo:
            self.apagar()
        else:
            self.encender()     
  

    #Getters y Setters
    def set_nombre_dispositivo(self, nombre_dispositivo):
        self.__nombre_dispositivo = nombre_dispositivo

    def get_nombre_dispositivo(self):
        return self.__nombre_dispositivo
    
    def get_tipo(self):
        return self.__tipo_dispositivo
    
    def set_tipo(self, tipo_dispositivo):
        self.__tipo_dispositivo= tipo_dispositivo
    
    def get_estado(self):
        return "Encendido" if self.__estado_dispositivo else "Apagado"

    def set_estado(self, estado_dispositivo):
        self.__estado_dispositivo = estado_dispositivo
    
    
    def get_id(self):
        return self.__id


    #Estado
    def __str__(self):
        return f"Dispositivo: {self.__nombre_dispositivo}, Tipo: {self.__tipo_dispositivo}, Estado: {'Encendido' if self.__estado_dispositivo else 'Apagado'}"
        
