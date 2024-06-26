from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import OperationalError
import os
from dotenv import load_dotenv



load_dotenv()



class Connection:

    SERVER_TYPE = os.getenv("SERVER_TYPE")
    LIBRARY_SERVER = os.getenv("LIBRARY_SERVER")
    SQL_USER = os.getenv("SQLUSER")
    SQL_PASSWORD = os.getenv("PASSWORD")
    SQL_SERVER = os.getenv("HOST")
    SQL_PORT = os.getenv("PORTSQL")
    SQL_DB = os.getenv("DATABASE")


    SQLALCHEMY_DATABASE_URL = f"{SERVER_TYPE}+{LIBRARY_SERVER}://{SQL_USER}:{SQL_PASSWORD}@{SQL_SERVER}:{SQL_PORT}/{SQL_DB}"
    print(SQLALCHEMY_DATABASE_URL)
    

    engine = create_engine(SQLALCHEMY_DATABASE_URL)

        
    try:
        engine.connect()
        sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        print("Conexión exitosa a la base de datos")
    except OperationalError as e:
        print(f"Error al conectar a la base de datos: {e}")
    



    Base = declarative_base()

class Connect:

    @staticmethod
    def get_db ():
        db = Connection.sessionlocal()
        print("nueva conexion", db)
        try:
            yield db
        finally: # finalizamos las conexiones
           
            print("cierra conexion")
            db.close()



    

