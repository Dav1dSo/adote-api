from src.models.mysql.repositories.pets_repository import PetsRepositoryInterface
from .interfaces.pet_delete_controller import PetDeleterControllerInterface

class PetDeleterController(PetDeleterControllerInterface):
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self._pet_repository = pet_repository

    def delete(self, name: str) -> None:
        self._pet_repository.delete_pet(name)
