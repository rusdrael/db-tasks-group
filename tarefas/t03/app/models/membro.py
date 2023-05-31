from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base_model import Base

class Membro(Base):
    __tablename__ = "membros"

    codigo: int = Column(Integer, primary_key=True, index=True)
    codEquipe: int = Column(Integer, ForeignKey("equipes.codigo"))
    codFuncionario: int = Column(Integer, ForeignKey("funcionarios.codigo"))
    membro_equipe = relationship('Equipe', backref='membros')
    funcionario = relationship('Funcionario', backref='membros')