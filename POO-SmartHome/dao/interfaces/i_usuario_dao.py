from abc import ABC, abstractmethod
from dominio.usuario import Usuario

class IUsuarioDAO(ABC):

    @abstractmethod
    def crear_usuario(self, usuario: Usuario):
        pass                 
    
    @abstractmethod
    def obtener_usuario_por_id(self, id_usuario: int):
        pass

    @abstractmethod
    def modificar_usuario(self, usuario: Usuario):
        pass

    @abstractmethod
    def eliminar_usuario(self, id_usuario: int):
        pass

    @abstractmethod
    def listar_usuarios(self):
        pass
