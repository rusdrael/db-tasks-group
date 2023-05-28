from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from app.database.base_model import Base

class AtividadeMembro(Base):
    __tablename__ = "atividade_membro"
    __table_args__ = (
        PrimaryKeyConstraint('codAtividade', 'codMembro'),
    )

    codAtividade: int = Column(Integer, ForeignKey("atividades.codigo"))
    atividade = relationship("Atividade", back_populates="atividade_membro")
    codMembro: int = Column(Integer, ForeignKey("membros.codigo"))
    projeto = relationship("Membro", back_populates="atividade_membro")