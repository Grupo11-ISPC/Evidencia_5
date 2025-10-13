class Usuario:
    def __init__(self, nombre, email, password, rol,id=None):
        if not Usuario.validar_usuario(nombre, email, password, rol):
            raise ValueError("Datos de usuario inválidos.")
        self.__id = id
        self.__nombre = nombre
        self.__email = email
        self.__password = password
        self.__rol = rol
        self.__dispositivos = []
        self.__automatizaciones = []
        

    def agregar_dispositivo(self, dispositivo):
        self.__dispositivos.append(dispositivo)
        return f"Dispositivo {dispositivo.get_nombre_dispositivo()} agregado."
    
    def eliminar_dispositivo(self, dispositivo):
        if dispositivo in self.__dispositivos:
            self.__dispositivos.remove(dispositivo)
            return f"Dispositivo {dispositivo.get_nombre_dispositivo()} eliminado."
        return "Dispositivo no encontrado."     
    
    def agregar_automatizacion(self, automatizacion):
        self.__automatizaciones.append(automatizacion)
        return f"Automatización {automatizacion.get_descripcion()} agregada."
    
    def listar_dispositivos(self):
        return [dispositivo.get_nombre_dispositivo() for dispositivo in self.__dispositivos]
    
    def listar_automatizaciones(self):
        return [automatizacion.get_descripcion() for automatizacion in self.__automatizaciones]
    
    def get_nombre(self):
        return self.__nombre
    
    def get_email(self):
        return self.__email
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    def ejecutar_automatizaciones(self):
        resultados = []
        for automatizacion in self.__automatizaciones:
            resultados.extend(automatizacion.ejecutar(self.__dispositivos))
        return resultados
    
    def ejecutar_accion_en_dispositivo(self, dispositivo_nombre, accion):
        for dispositivo in self.__dispositivos:
            if dispositivo.get_nombre_dispositivo() == dispositivo_nombre:
                return dispositivo.ejecutar_accion(accion)
        return "Dispositivo no encontrado." 

    @staticmethod #para que no necesite self, osea, para que se valide sin instanciar la clase(crear el objeto)
    def validar_usuario(nombre, email, password, rol):
        if not nombre or not email or not password or not rol:
            return False
        if "@" not in email or "." not in email.split("@")[-1]:
            return False
        if len(password) < 6:
            return False
        if rol not in ['admin', 'user']:
            return False
        return True
    
    def get_rol(self):
        return self.__rol
    
    def set_rol(self, rol):
        self.__rol = rol
