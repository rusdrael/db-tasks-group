from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from app.database.base_model import Base

class AtividadeMembro(Base):
    __tablename__ = "atividade_membro"
    __table_args__ = (
        PrimaryKeyConstraint('codAtividade', 'codMembro'),
    )

    codAtividade: int = Column(Integer, ForeignKey("atividades.codigo"))
    codMembro: int = Column(Integer, ForeignKey("membros.codigo"))

    atividade = relationship('Atividade', backref='atividade_atividade')
    membro = relationship('Membro', backref='atv_membro')