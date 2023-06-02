from datetime import datetime
from app.models.atividade import Atividade
from app.models.atividade_projeto import AtividadeProjeto
from app.models.funcionario import Funcionario
from app.models.membro import Membro
from app.models.projeto import Projeto
from app.database.session import get_db

def generate_project_report():
    # Consulta para obter informações dos projetos

    # Exibição das informações
    for projeto in get_db.query(Projeto):
        id_responsavel = projeto.responsavel_id
        nome_gerente = None
        qtd_membros_equipe = 0
        qtd_atividades = 0
        qtd_atividades_atrasadas = 0
        data_atual = datetime.now()
        soma_atraso_atividades = 0
        atraso = data_atual - projeto.dataFim
        
        for funcionario in get_db.query(Funcionario):
            if funcionario.codigo == id_responsavel:
                nome_gerente = funcionario.nome
        
        for membro in get_db.query(Membro):
            if projeto.equipe_id == membro.codEquipe_id:
                qtd_membros_equipe += 1
        
        for atividade_projeto in get_db.query(AtividadeProjeto):
            if projeto.codigo == atividade_projeto.codProjeto:
                qtd_atividades += 1
                for atividade in get_db.query(Atividade):
                    if (atividade.codigo == atividade_projeto.codAtividade) and atividade.situacao.lower() != "concluído":
                        qtd_atividades_atrasadas += 1
                        atraso_atividade = data_atual - atividade.dataFim
                        soma_atraso_atividades += atraso_atividade.days

        print(f"Código do Projeto: {projeto.codigo}")
        print(f"Nome do Projeto: {projeto.descricao}")
        print(f"Nome do Gerente: {nome_gerente}")
        print(f"Quantidade de Membros da Equipe: {qtd_membros_equipe}")
        print("O atraso em dias é:", atraso.days if projeto.situacao.lower() != "concluído" and atraso.days > 0 else "N/A")
        print("A quantidade de atividades no projeto é:", qtd_atividades)
        print("A quantidade de atividades não concluídas no projeto é:", qtd_atividades_atrasadas)
        print("A soma de dias das atividades atrasadas é:", soma_atraso_atividades if soma_atraso_atividades > 0 else "N/A")
        print("---------------------------------------------------")


def run_project_report():
    # Consulta para obter informações dos projetos

    # Exibição das informações
    for projeto in get_db.query(Projeto):
        id_responsavel = projeto.responsavel_id
        nome_gerente = None
        qtd_membros_equipe = 0
        qtd_atividades = 0
        qtd_atividades_atrasadas = 0
        data_atual = datetime.now()
        soma_atraso_atividades = 0
        atraso = data_atual - projeto.dataFim
        
        for funcionario in get_db.query(Funcionario):
            if funcionario.codigo == id_responsavel:
                nome_gerente = funcionario.nome
        
        for membro in get_db.query(Membro):
            if projeto.equipe_id == membro.codEquipe_id:
                qtd_membros_equipe += 1
        
        for atividade_projeto in get_db.query(AtividadeProjeto):
            if projeto.codigo == atividade_projeto.codProjeto:
                qtd_atividades += 1
                for atividade in get_db.query(Atividade):
                    if (atividade.codigo == atividade_projeto.codAtividade) and atividade.situacao.lower() != "concluído":
                        qtd_atividades_atrasadas += 1
                        atraso_atividade = data_atual - atividade.dataFim
                        soma_atraso_atividades += atraso_atividade.days

# Chamada do procedimento

if __name__ == '__main__':
    generate_project_report()