from typing import Any

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr

class Base(DeclarativeBase):
    id: Any
    __name__: str
    __allow_unmaped__ = True

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()

class Tasks(Base):
    __tablename__ = 'Tasks'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)  # желательно явно указать
    name: Mapped[str]
    pomodoro_count: Mapped[int]
    category_id: Mapped[int]

class Categories(Base):
    __tablename__ = 'Categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str]
    name: Mapped[str]