from app.database.session import get_db
from app.database.relatorio import gera_relatorio_do_projeto
from app.models.log import Log

import time

def obter_primeiros_mil_registros(db: Session = Depends(get_db)):
    get_func = db.query(Funcionario).limit(1000).all()
    get_dep = db.query(Departamento).limit(1000).all()
    get_atv = db.query(Atividade).limit(1000).all()
    get_proj = db.query(Projeto).limit(1000).all()

def calcular_tempo_execucao(func, db: Session = Depends(get_db)):
    start = time.time()
    func()
    end = time.time()
    return end - start

def registrar_tempo_execucao(db: Session = Depends(get_db)):
    logs = db.query(Log).all()
    num = len(logs)

    db.add(Log(
        log="Log " + str(num),
        time=calcular_tempo_execucao(obter_primeiros_mil_registros)
    ))
    db.commit()

def registrar_tempo_geracao_relatorio(db: Session = Depends(get_db)):
    logs = db.query(Log).all()
    num = len(logs)

    db.add(Log(
        log="Log " + str(num),
        time=calcular_tempo_execucao(gera_relatorio_do_projeto)
    ))
    db.commit()
    
if __name__ == '__main__':
    registrar_tempo_execucao()
    registrar_tempo_geracao_relatorio()