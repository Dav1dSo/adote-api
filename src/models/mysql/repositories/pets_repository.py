from sqlalchemy.orm.exc import NoResultFound
from src.models.mysql.entities.pets import PetsTable

class PetsRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
        
    def pets_list(self) -> list[PetsTable]:
        with self.__db_connection as database:
            try:
                pets = database.session.query(PetsTable).all()
                return pets
            except NoResultFound:
                return []
        
    def pet_delete(self, pet_id):
        with self.__db_connection as database:
            try:
                database.session.query(PetsTable).filter_by(id=pet_id).delete()
                database.session.commit()
            except Exception as err:
                database.session.rollback()
                raise err