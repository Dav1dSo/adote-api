from .person_create_controller import PersonCreateController
import pytest

class MockPeopleRepository:
    def insert_person(seld, first_name: str, last_name: str, age: int, pet_id: int):
        pass
    
def test_create_person():
        data_person = {
            "first_name": "Nome",
            "last_name": "Nomeal",
            "age": 20,
            "pet_id": 3
        }
        
        controller = PersonCreateController(MockPeopleRepository())
        
        response = controller.insert_person(data_person)
        
        assert response["data"]["type"] == "Person"
        assert response["data"]["count"] == 1
        assert response["data"]["attributes"] == data_person
        
        
def test_create_person_error():
        data_person = {
            "first_name": "Nome57",
            "last_name": "Nomeal-",
            "age": 20,
            "pet_id": 3
        }
        
        controller = PersonCreateController(MockPeopleRepository())
        
        with pytest.raises(Exception):
            controller.insert_person(data_person)
        