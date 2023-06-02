from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from app.database.base_model import Base

class AtividadeProjeto(Base):
    __tablename__ = "atividade_projeto"
    __table_args__ = (
        PrimaryKeyConstraint('codAtividade', 'codProjeto'),
    )

    codAtividade: int = Column(Integer, ForeignKey("atividades.codigo"), index=True)
    codProjeto: int = Column(Integer, ForeignKey("projetos.codigo"), index=True)
    atividade = relationship('Atividade', backref='atividade_projeto')
    projeto = relationship('Projeto', backref='atividade_projeto')