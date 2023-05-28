from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from app.database.base_model import Base

class AtividadeProjeto(Base):
    __tablename__ = "atividade_projeto"
    __table_args__ = (
        PrimaryKeyConstraint('codAtividade', 'codProjeto'),
    )

    codAtividade: int = Column(Integer, ForeignKey("atividades.codigo"))
    atividade = relationship("Atividade", back_populates="atividade_projeto")
    codProjeto: int = Column(Integer, ForeignKey("projetos.codigo"))
    projeto = relationship("Projeto", back_populates="atividade_projeto")

