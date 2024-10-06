from src.models.mysql.interfaces.people_repository_interface import PeopleRepositoryInterface
from src.models.mysql.entities.people import PeopleTable 
from .interfaces.person_finder_controller import PersonFinderControllerInterface

class PersonFinderController(PersonFinderControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository
        
    def find(self, person_id: int) -> dict:
        person = self.__find_person_in_db(person_id=person_id)
        response = self.__format_response(person=person)
        return response
    
    def __find_person_in_db(self, person_id: int) -> PeopleTable:   
        person = self.__people_repository.get_person(person_id=person_id)
        
        if not person:
            raise Exception("Pessoa não encontrada")
        
        return person
    
    def __format_response(self, person: PeopleTable) -> dict:           
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes" : {
                    "first name": person.first_name,
                    "last_name": person.last_name,
                    "pet_name": person.pet_name,
                    "pet_type": person.pet_type
                    }
                }
            }