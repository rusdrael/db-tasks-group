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
    responsavel_id: int = Column(Integer, ForeignKey("funcionarios.codigo"))
    equipe_id: int = Column(Integer, ForeignKey("equipes.codigo"))
    depto = relationship('Departamento', backref='projetos')
    responsavel = relationship('Funcionario', backref='projetos')
    equipe = relationship('Equipe', backref='projetos')