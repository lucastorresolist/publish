import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Session:
    def __init__(self):
        load_dotenv()
        connector = os.getenv('PG_CONNECTOR')
        host = os.getenv('PG_HOST')
        user = os.getenv('PG_USER')
        password = os.getenv('PG_PASSWORD')
        dbname = os.getenv('PG_DATABASE')
        self.__connection_string = f"{connector}://{user}:{password}@{host}:5432/{dbname}"

    def __enter__(self):
        self.__engine = create_engine(self.__connection_string)
        Session = sessionmaker(self.__engine)
        self.__session = Session()
        return self.__session

    def __exit__(self, type, value, trace):
        self.__session.close()
        self.__engine.dispose()