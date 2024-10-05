from src.models.mysql.settings.connection import db_connection_handler
from .pets_repository import PetsRepository

db_connection_handler.connect_to_db()

def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.pets_list()
    
    print(response)
    
def test_delete_pet():
    pet_id = 7
    repo = PetsRepository(db_connection_handler)
    response = repo.pet_delete(pet_id)