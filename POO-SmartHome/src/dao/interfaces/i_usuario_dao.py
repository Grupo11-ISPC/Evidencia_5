from abc import ABC, abstractmethod
from dominio.usuario import Usuario

class IUsuarioDAO(ABC):
    @abstractmethod
    def guardar(self, usuario: Usuario):
        pass

    @abstractmethod
    def obtener_por_id(self, id: int):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def modificar(self, usuario: Usuario):
        pass

    @abstractmethod
    def eliminar(self, usuario: Usuario):
        pass
