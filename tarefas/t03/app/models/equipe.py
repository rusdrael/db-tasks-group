from sqlalchemy import Column, Integer, String
from app.database.base_model import Base

class Equipe(Base):
    __tablename__ = "equipes"

    codigo: int = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nomeEquipe: str = Column(String(45), unique=True, nullable=False)
