from sqlalchemy import Column, Integer, String, Numeric
from app.database.base_model import Base

class Log(Base):
    __tablename__ = 'log'

    codigo = Column(Integer, primary_key=True, autoincrement=True)
    log = Column(String, nullable=False)
    time = Column(Numeric, nullable=False)