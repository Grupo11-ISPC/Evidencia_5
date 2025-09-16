from accion import Accion

class Dispositivo:
    def __init__(self, nombre_dispositivo, tipo_dispositivo, estado_dispositivo = False):
        self.nombre_dispositivo = nombre_dispositivo
        self.tipo_dispositivo = tipo_dispositivo
        self.estado_dispositivo = estado_dispositivo

    #Acciones
    def ejecutar_accion(self, accion):
        if accion.tipo_accion == "encender":
            self.encender()
            return f"El dispositivo {self.nombre_dispositivo} ha sido encendido."
        
        elif accion.tipo_accion == "apagar":
            self.apagar()
            return f"El dispositivo {self.nombre_dispositivo} ha sido apagado."
        
        elif accion.tipo_accion == "cambiar_estado":
            self.cambiar_estado()
            return f"El dispositivo {self.nombre_dispositivo} ha cambiado su estado."
        
        elif accion.tipo_accion == "set_nombre":
            self.set_nombre_dispositivo(accion.valor_configurado)
            return f"El dispositivo ahora se llama {self.nombre_dispositivo}."
        
        elif accion.tipo_accion == "set_tipo":
            self.set_tipo(accion.valor_configurado)
            return f"El dispositivo ahora es de tipo {self.tipo_dispositivo}."
        
        elif accion.tipo_accion == "set_estado":
            self.set_estado(accion.valor_configurado)
            return f"El estado del dispositivo se configuró como {self.estado_dispositivo}."
        
        else:
            return "Acción no reconocida."

   
    def encender(self):
        self.estado_dispositivo = True
    
    def apagar(self):
        self.estado_dispositivo = False

    def cambiar_estado(self):
        if self.estado_dispositivo:
            self.apagar()
        else:
            self.encender()          

    #Getters y Setters
    def set_nombre_dispositivo(self, nombre_dispositivo):
        self.nombre_dispositivo = nombre_dispositivo

    def get_nombre_dispositivo(self):
        return self.nombre_dispositivo
    
    def get_tipo(self):
        return self.tipo_dispositivo
    
    def set_tipo(self, tipo_dispositivo):
        self.tipo_dispositivo= tipo_dispositivo
    
    def get_estado(self):
        return self.estado_dispositivo

    def set_estado(self, estado_dispositivo):
        self.estado_dispositivo = estado_dispositivo

    #Estado
    def __str__(self):
        return f"Dispositivo: {self.nombre_dispositivo}, Tipo: {self.tipo_dispositivo}, Estado: {'Encendido' if self.estado_dispositivo else 'Apagado'}"
        
