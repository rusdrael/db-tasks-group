from fastapi import APIRouter, Depends
from app.database.odbc import session

router = APIRouter(tags=["Status"])

@router.get("/odbc/{projeto_codigo}/atividades")
async def atividades_de_projeto(projeto_codigo, db = Depends(session)):
    cursor = db.cursor()
    cursor.execute("SELECT FROM empresa_db.atividades a JOIN empresa_db.atividade_projeto ap ON a.codigo = ap.codAtividade WHERE ap.codProjeto = ?", projeto_codigo) 
    atividades_projetos = cursor.fetchall()
    cursor.close()
    db.close()

    return atividades_projetos
