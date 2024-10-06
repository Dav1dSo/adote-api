from abc import ABC, abstractmethod
from src.models.mysql.entities.people import PeopleTable

class PeopleRepositoryInterface(ABC):
    
    @abstractmethod
    def insert_person(self, data) -> None:
        pass
    
    @abstractmethod
    def get_person(self, person_id) -> PeopleTable:
        pass