from sqlalchemy import Column, Integer, String, Date
from app.database.base_model import Base

class Atividade(Base):
    __tablename__ = "atividades"

    codigo: int = Column(Integer, primary_key=True, index=True)
    descricao: str = Column(String(45))
    dataInicio = Column(Date)
    dataFim = Column(Date, index=True)
    situacao: str = Column(String(255), index=True)
    dataConclusao = Column(Date)