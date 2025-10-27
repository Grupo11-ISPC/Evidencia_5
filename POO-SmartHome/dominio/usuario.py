class Usuario:
    def __init__(self, nombre, email, password, rol, id=None):
        self.__id = id
        self.__nombre = nombre
        self.__email = email
        self.__password = password
        self.__rol = rol

    def get_id(self):
        return self.__id
        
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

    def get_password(self):
        return self.__password
    
    def get_rol(self):
        return self.__rol
    
    def set_rol(self, rol):
        self.__rol = rol

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
