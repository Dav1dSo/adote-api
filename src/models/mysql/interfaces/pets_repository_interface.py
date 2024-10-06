from abc import ABC, abstractmethod
from src.models.mysql.entities.pets import PetsTable


class PetsRepositoryInterface(ABC):
    @abstractmethod
    def pets_list(self) -> list[PetsTable]:
        pass
    
    @abstractmethod
    def pet_delete(self, pet_id: int) -> None:
        pass
        