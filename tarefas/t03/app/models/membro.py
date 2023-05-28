from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base_model import Base

class Membro(Base):
    __tablename__ = "membros"

    codigo: int = Column(Integer, primary_key=True, index=True)
    codEquipe: int = Column(Integer, ForeignKey("equipes.codigo"))
    equipe = relationship("Equipe", back_populates="membro")
    codFuncionario: int = Column(Integer, ForeignKey("funcionarios.codigo"))
    funcionario = relationship("Funcionario", back_populates="membro")