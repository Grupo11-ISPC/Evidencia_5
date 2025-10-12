from abc import ABC, abstractmethod
from dominio.dispositivo import Dispositivo

class IDispositivoDAO(ABC):
    @abstractmethod
    def guardar(self, dispositivo: Dispositivo, usuario_id=None):
        pass

    @abstractmethod
    def obtener_por_id(self, id: int):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def modificar(self, dispositivo: Dispositivo):
        pass

    @abstractmethod
    def eliminar(self, dispositivo: Dispositivo):
        pass
