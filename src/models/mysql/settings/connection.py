import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

class DBConnerctionHandler:
    def __init__(self) -> None:
        self.__connection_string = DATABASE_URL 

        self.__engine = None 
            
    def connect_to_db(self):
        self.__engine = create_engine(self.__connection_string)
        
    def get_engine(self):
        return self.__engine

db_connection_handler = DBConnerctionHandler()
    