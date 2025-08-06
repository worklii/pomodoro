import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import settings  # импортируем экземпляр settings


engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5433/pomodoro')
Session = sessionmaker(engine)
def get_db_session() -> Session:
    return Session