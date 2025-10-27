from abc import ABC, abstractmethod
from dominio.dispositivo import Dispositivo

class IDispositivoDAO(ABC):
    @abstractmethod
    def crear_dispositivo(self, dispositivo: Dispositivo, id_usuario: int):
        pass

    @abstractmethod
    def obtener_por_id(self, id: int):
        pass

    @abstractmethod
    def listar_dispositivo(self):
        pass

    @abstractmethod
    def modificar_dispositivo(self, dispositivo: Dispositivo):
        pass

    @abstractmethod
    def eliminar_dispositivo(self, id: int):
        pass

    @abstractmethod
    def get_nombre_dispositivo(self, id: int):
        pass