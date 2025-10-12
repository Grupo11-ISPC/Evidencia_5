class Accion:
    def __init__(self, tipo_accion, valor_configurado):
        self.__tipo_accion = tipo_accion
        self.__valor_configurado = valor_configurado

    def __str__(self):
        return f"Accion: {self.__tipo_accion}, Valor Configurado: {self.__valor_configurado}"
    
    def get_tipo_accion(self):
        return self.__tipo_accion
    
    def get_valor_configurado(self):
        return self.__valor_configurado
    
    def set_tipo_accion(self, tipo_accion):
        self.__tipo_accion = tipo_accion
        
    def set_valor_configurado(self, valor_configurado):
        self.__valor_configurado = valor_configurado

    def realizar_accion(self):
        return f"Realizando acción: {self.__tipo_accion} con valor: {self.__valor_configurado}"
