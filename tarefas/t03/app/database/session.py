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

    Base.metadata.create_all(engine)


def create_session() -> Session:
    global __factory

    if not __factory:
        raise Exception("You must call global_init() before using this method")

    session: Session = __factory()
    session.expire_on_commit = False

    return session


def populate_db(db):
    fake = Faker()
    print("populate")

    departamentos = []
    for _ in range(5):
        departamento = Departamento(
            sigla=fake.word().upper(),
            descricao=fake.sentence(),
            gerente=fake.name()
        )
        departamentos.append(departamento)
    db.bulk_save_objects(departamentos)
    db.commit()

    # Equipe
    equipes = []
    for _ in range(10):
        equipe = Equipe(
            nomeEquipe=fake.job()
        )
        equipes.append(equipe)
    db.bulk_save_objects(equipes)
    db.commit()

    # Funcionario
    funcionarios = []
    for _ in range(20):
        funcionario = Funcionario(
            nome=fake.name(),
            sexo=random.choice(['M', 'F']),
            dataNasc=fake.date_of_birth(minimum_age=18, maximum_age=65),
            salario=random.uniform(1000, 5000),
            supervisor=fake.name(),
            depto=random.choice(departamentos).codigo
        )
        funcionarios.append(funcionario)
    db.bulk_save_objects(funcionarios)
    db.commit()

    # Membro
    membros = []
    for funcionario in funcionarios:
        membro = Membro(
            codEquipe=random.choice(equipes).codigo,
            codFuncionario=funcionario.codigo
        )
        membros.append(membro)
    db.bulk_save_objects(membros)
    db.commit()

    # Projeto
    projetos = []
    for _ in range(5):
        projeto = Projeto(
            descricao=fake.sentence(),
            depto=random.choice(departamentos).codigo,
            responsavel=fake.name(),
            dataInicio=fake.date_time_between(start_date='-5y', end_date='now', tzinfo=None),
            dataFim=fake.date_time_between(start_date='now', end_date='+5y', tzinfo=None),
            situacao=random.choice(['Em andamento', 'Concluído']),
            dataConclusao=fake.date_time_between(start_date='-5y', end_date='now', tzinfo=None),
            equipe=random.choice(equipes).codigo
        )
        projetos.append(projeto)
    db.bulk_save_objects(projetos)
    db.commit()

    # Atividade
    atividades = []
    for projeto in projetos:
        atividade = Atividade(
            descricao=fake.sentence(),
            dataInicio=fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None),
            dataFim=fake.date_time_between(start_date='now', end_date='+1y', tzinfo=None),
            situacao=random.choice(['Em andamento', 'Concluída']),
            dataConclusao=fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
        )
        atividades.append(atividade)
        atividade_projeto = AtividadeProjeto(
            codAtividade=atividade.codigo,
            codProjeto=projeto.codigo
        )
        db.add(atividade_projeto)
        db.bulk_save_objects(atividades)
    db.commit()