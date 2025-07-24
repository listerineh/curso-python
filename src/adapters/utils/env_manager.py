import os
from dotenv import load_dotenv


class Settings:
    def __init__(self):
        load_dotenv()
        
        try:
            self.postgres_dbname=os.getenv('POSTGRES-DBNAME', 'curso-python')
            self.postgres_user=os.getenv('POSTGRES-USER', 'root')
            self.postgres_password=os.getenv('POSTGRES-PASSWORD', 'root')
            self.postgres_host=os.getenv('POSTGRES-HOST', 'localhost')
            self.postgres_port=os.getenv('POSTGRES-PORT', '5432')
        except Exception as e:
            raise e


def get_settings():
    return Settings()
