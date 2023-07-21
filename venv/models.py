from db import Base
from sqlalchemy import Column, Integer, String

class Pessoa(Base):
    __tablename__ = 'pessoas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    linkedin = Column(String(200), nullable=False)
    github = Column(String(200), nullable=False)

    def __repr__(self):
        return f'<Person {self.nome}>'
