from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import Settings  # импортируем экземпляр settings

settings = Settings()

engine = create_engine(settings.db_url)
Session = sessionmaker(engine)
def get_db_session() -> Session:
    return Session