from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.database.base_model import Base

class AtividadeProjeto(Base):
    __tablename__ = "atividade_projeto"
    __table_args__ = (
        PrimaryKeyConstraint('codAtividade', 'codProjeto'),
    )

    codAtividade: int = Column(Integer, ForeignKey("atividades.codigo"))
    codProjeto: int = Column(Integer, ForeignKey("projetos.codigo"))

    atividade = relationship('Atividade', backref='atv_projeto')
    projeto = relationship('Projeto', backref='projeto_atv')