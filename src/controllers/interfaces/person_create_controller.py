from typing import Dict
from abc import ABC, abstractmethod

class PersonCreateControllerInterface(ABC):
    @abstractmethod
    def insert_person(self, person_info: Dict) -> Dict:
        pass
