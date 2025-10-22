class Usuario:
    def __init__(self, nombre, email, password, rol, id=None):
        self._id = id
        self._nombre = nombre
        self._email = email
        self._password = password
        self._rol = rol

    def get_id(self):
        return self._id
        
    def get_nombre(self):
        return self._nombre
    
    def get_email(self):
        return self._email
    
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_email(self, email):
        self._email = email

    def set_password(self, password):
        self._password = password

    def get_password(self):
        return self._password
    
    def get_rol(self):
        return self._rol
    
    def set_rol(self, rol):
        self._rol = rol

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
