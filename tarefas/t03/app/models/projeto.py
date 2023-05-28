from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base_model import Base

class Projeto(Base):
    __tablename__ = "projetos"

    codigo: int = Column(Integer, primary_key=True, index=True)
    descricao: str = Column(String(45))
    dataInicio = Column(Date)
    dataFim = Column(Date)
    situacao: str = Column(String(255))
    dataConclusao = Column(Date)
    depto_id: int = Column(Integer, ForeignKey("departamentos.codigo"))
    depto = relationship("Departamento", back_populates="projeto")
    responsavel_id: int = Column(Integer, ForeignKey("funcionarios.codigo"))
    responsavel = relationship("Funcionario", back_populates="projeto")
    equipe_id: int = Column(Integer, ForeignKey("equipes.codigo"))
    equipe = relationship("Equipe", back_populates="projeto")