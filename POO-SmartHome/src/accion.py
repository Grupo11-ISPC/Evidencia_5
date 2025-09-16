class Accion:
    def __init__(self, tipo_accion, valor_configurado):
        self.tipo_accion = tipo_accion
        self.valor_configurado = valor_configurado

    def __str__(self):
        return f"Accion: {self.tipo_accion}, Valor Configurado: {self.valor_configurado}"
    
    def get_tipo_accion(self):
        return self.tipo_accion
    
    def get_valor_configurado(self):
        return self.valor_configurado
    
    def set_tipo_accion(self, tipo_accion):
        self.tipo_accion = tipo_accion
        
    def set_valor_configurado(self, valor_configurado):
        self.valor_configurado = valor_configurado

    def realizar_accion(self):
        return f"Realizando acción: {self.tipo_accion} con valor: {self.valor_configurado}"
