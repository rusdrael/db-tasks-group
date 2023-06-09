from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base_model import Base

class Funcionario(Base):
    __tablename__ = "funcionarios"

    codigo: int = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome: str = Column(String(255), nullable=False)
    sexo: str = Column(String(1))
    dataNasc = Column(Date)
    salario: str = Column(String(255))
    supervisor_id: int = Column(Integer, ForeignKey("funcionarios.codigo"))
    depto_id: int = Column(Integer, ForeignKey("departamentos.codigo"))
    supervisor = relationship('Funcionario', backref='funcionarios')
    depto = relationship('Departamento', backref='funcionarios')
