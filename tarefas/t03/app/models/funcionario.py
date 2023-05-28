from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base_model import Base

class Funcionario(Base):
    __tablename__ = "funcionarios"

    codigo: int = Column(Integer, primary_key=True, index=True)
    nome: str = Column(String(255), nullable=False)
    sexo: str = Column(String(1))
    dataNasc = Column(Date)
    salario: str = Column(String(255))
    supervisor_id: int = Column(Integer, ForeignKey("funcionarios.codigo"))
    supervisor = relationship("Funcionario", back_populates="funcionario")
    depto_id: int = Column(Integer, ForeignKey("departamentos.codigo"))
    depto = relationship("Departamento", back_populates="funcionario")
