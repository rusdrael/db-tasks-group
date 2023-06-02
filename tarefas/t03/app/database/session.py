import logging
from typing import Callable, Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.database.base_model import Base

__factory: Optional[Callable[[], Session]] = None
log = logging.getLogger("uvicorn")


def get_db() -> Session:
    db = create_session()
    try:
        yield db
    finally:
        db.close()


def global_init() -> None:
    global __factory

    if __factory:
        return

    log.info("Connecting to the database...")
    import pyodbc
    engine = create_engine('postgresql://root:password@localhost:5400/empresa_db', echo=False)
    __factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    from app.models.atividade import Atividade
    from app.models.departamento import Departamento
    from app.models.equipe import Equipe
    from app.models.funcionario import Funcionario
    from app.models.membro import Membro
    from app.models.projeto import Projeto
    from app.models.atividade_membro import AtividadeMembro
    from app.models.atividade_projeto import AtividadeProjeto
    from app.models.log import Log

    Base.metadata.create_all(engine)


def create_session() -> Session:
    global __factory

    if not __factory:
        raise Exception("You must call global_init() before using this method")

    session: Session = __factory()
    session.expire_on_commit = False

    return session
