class Usuario:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password
        self.dispositivos = []
        self.automatizaciones = []
        if not Usuario.validar_usuario(nombre, email, password):
            raise ValueError("Datos de usuario inválidos.")
    
    def agregar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)
        return f"Dispositivo {dispositivo.get_nombre_dispositivo()} agregado."
    
    def agregar_automatizacion(self, automatizacion):
        self.automatizaciones.append(automatizacion)
        return f"Automatización {automatizacion.get_descripcion()} agregada."
    def listar_dispositivos(self):
        return [dispositivo.get_nombre_dispositivo() for dispositivo in self.dispositivos]
    
    def listar_automatizaciones(self):
        return [automatizacion.get_descripcion() for automatizacion in self.automatizaciones]
    
    def get_nombre(self):
        return self.nombre
    
    def get_email(self):
        return self.email
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password

    def ejecutar_automatizaciones(self):
        resultados = []
        for automatizacion in self.automatizaciones:
            resultados.extend(automatizacion.ejecutar(self.dispositivos))
        return resultados
    
    def ejecutar_accion_en_dispositivo(self, dispositivo_nombre, accion):
        for dispositivo in self.dispositivos:
            if dispositivo.get_nombre_dispositivo() == dispositivo_nombre:
                return dispositivo.ejecutar_accion(accion)
        return "Dispositivo no encontrado."
    
    def __str__(self):
        return f"Usuario: {self.nombre}, Email: {self.email}"
    
    def validar_usuario(nombre, email, password):
        if not nombre or not email or not password:
            return False
        if "@" not in email or "." not in email.split("@")[-1]:
            return False
        if len(password) < 6:
            return False
        return True