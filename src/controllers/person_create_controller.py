import re
from src.models.mysql.entities.people import PeopleTable
from src.models.mysql.interfaces.people_repository_interface import (
    PeopleRepositoryInterface,
)
from .interfaces.person_create_controller import PersonCreateControllerInterface

class PersonCreateController(PersonCreateControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def insert_person(self, data: dict) -> dict:
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        age = data.get("age")
        pet_id = data.get("pet_id")

        self.__validate_first_and_last_name(first_name, last_name)
        self.__insert_person_in_db(first_name, last_name, age, pet_id)
        response = self.__format_reponse(person_info=data)
        return response
    
    def __validate_first_and_last_name(self, first_name: str, last_name: str) -> None:
        non_valid_caracteres = re.compile(r"[^a-zA-Z]")

        if non_valid_caracteres.search(first_name) or non_valid_caracteres.search(last_name):
            raise Exception("Nome da pessoa inválido!")

    def __insert_person_in_db(self, first_name: str, last_name: str, age: int, pet_id: int):
        self.__people_repository.insert_person(first_name, last_name, age, pet_id)
    
    def __format_reponse(self, person_info: dict) -> dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_info
            }
        }