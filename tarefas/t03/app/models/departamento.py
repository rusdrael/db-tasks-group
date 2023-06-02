from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base_model import Base

class Departamento(Base):
    __tablename__ = "departamentos"

    codigo: int = Column(Integer, primary_key=True, autoincrement=True, index=True)
    sigla: str = Column(String(15), unique=True, nullable=False)
    descricao: str = Column(String(25), nullable=False)
    gerente_id: int = Column(Integer, ForeignKey("funcionarios.codigo"))
    gerente = relationship('Funcionario', backref='departamento')
