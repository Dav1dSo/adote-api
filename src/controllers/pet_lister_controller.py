from src.models.mysql.interfaces.pets_repository_interface import PetsRepositoryInterface
from src.models.mysql.entities.pets import PetsTable

class PetListController:
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository
        
    def list(self) -> dict:
        pets = self.__get_pets_in_db()
    
    def __get_pets_in_db(self) -> list[PetsTable]:
        pets = self.__pet_repository.pets_list()
        response = self.__format_response(pets)
        return response
    
    def __format_response(self, pets: list[PetsTable]) -> dict:
        formated_pets = [
            {
                "name": pet.name,
                "type": pet.type,
                "id": pet.id
            } for pet in pets
        ]
        
        return {
            "data": {
                "type": "Pets",
                "count": len(formated_pets),
                "attributes": formated_pets
            }
        }