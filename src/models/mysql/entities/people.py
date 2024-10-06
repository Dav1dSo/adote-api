from src.models.mysql.settings.base import Base
from sqlalchemy import Column, String, BIGINT, ForeignKey

class PeopleTable(Base):
    __tablename__ = "people"
    
    id = Column(BIGINT, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(BIGINT, nullable=False)
    pet_id = Column(BIGINT,  ForeignKey("pets.id"))