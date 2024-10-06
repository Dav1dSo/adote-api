from src.models.mysql.entities.people import PeopleTable
from src.models.mysql.entities.pets import PetsTable


class PeopleRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_person(self, data: dict) -> None:
        with self.__db_connection as database:
            try:
                perso_data = PeopleTable(
                    first_name=data["first_name"],
                    last_name=data["last_name"],
                    age=data["age"],
                    pet_id=data["pet_id"],
                )

                database.session.add(perso_data)
                database.session.commit()
            except Exception as err:
                database.session.rollback()
                raise err

    def get_person(self, person_id):
        with self.__db_connection as database:
            try:
                person = (
                    database.session.query(PeopleTable)
                    .outerjoin(PetsTable, PetsTable.id == PeopleTable.pet_id)
                    .filter(PeopleTable.id == person_id)
                    .with_entities(
                        PeopleTable.first_name,
                        PeopleTable.last_name,
                        PetsTable.name.label("pet_name"),
                        PetsTable.type.label("pet_type")
                    ).first()
                )
                
                return person
                
            except Exception as err:
                raise err
