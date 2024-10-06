from src.models.mysql.settings.connection import db_connection_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository

db_connection_handler.connect_to_db()

def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.pets_list()
    
    print(response)
    
def test_delete_pet():
    pet_id = 7
    repo = PetsRepository(db_connection_handler)
    response = repo.pet_delete(pet_id)
    

def test_crate_people():
    data = {
        "first_name": "test_name",
        "last_name": "name last",
        "age": 11,
        "pet_id": 2
    }    
    
    repo = PeopleRepository(db_connection_handler)
    repo.insert_person(data)
    
def test_get_person():
    repo = PeopleRepository(db_connection_handler)
    response = repo.get_person(1)
    
    print(response)