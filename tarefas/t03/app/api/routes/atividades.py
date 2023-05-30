from fastapi import APIRouter, Depends
from app.database.session import get_db, populate_db
from app.models.atividade import Atividade
from app.models.atividade_projeto import AtividadeProjeto 


router = APIRouter(tags=["Atividades"])

@router.get("/{projeto_codigo}/atividades")
async def atividades_de_projeto(projeto_codigo, db = Depends(get_db)):
    populate_db(db)
    return projeto_codigo
    # return db.query(Atividade).join(AtividadeProjeto).filter(AtividadeProjeto.codProjeto == projeto_codigo) is not None 