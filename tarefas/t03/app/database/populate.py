from app.models.atividade import Atividade
from app.models.atividade_projeto import AtividadeProjeto
from app.models.equipe import Equipe
from app.models.funcionario import Funcionario
from app.models.departamento import Departamento
from random import choice
from faker import Faker
from app.database.session import get_db

fake = Faker()

def populate_funcionario(num_rows):
    for i in range(int(num_rows)):
        name = fake.name()
        gender=fake.random_element(['M', 'F'])
        dob = fake.date_of_birth(minimum_age=18, maximum_age=90)
        salary = fake.pydecimal(left_digits=5, right_digits=2, positive=True)
        get_db.add (Funcionario(
            nome=name, 
            sexo=gender, 
            dataNasc=dob, 
            salario=salary
        )),
        get_db.commit()
    for f in get_db.query(Funcionario):
        if f.supervisor is None:
            supervisor = choice(get_db.query(Funcionario).filter(Funcionario != f).all())
            f.supervisor_id = supervisor.codigo
            get_db.commit()


def populate_departamento(num_rows):
    cont = len(get_db.query(Departamento).all())
    fixed_letters = 'DP' 
    fixed_dp = 'Departamento'
    for i in range( int (num_rows)):
        cont+=1
        third_character = cont 
        department = fixed_letters + str(third_character)
        description = fixed_dp + str(third_character)
        get_db.add(Departamento(
            sigla=department,
            descricao=description
        ))
        get_db.commit()
    for d in get_db.query(Departamento):
        if d.gerente is None:
            f = choice(get_db.query(Funcionario).all())
            d.gerente = f
            d.gerente_id= f.codigo
            get_db.commit()
    for f in get_db.query(Funcionario):
        if f.depto_id is None:
            dep= choice(get_db.query(Departamento).all())
            d_id= dep.codigo
            f.depto_id= d_id
            get_db.commit()

def populate_equipe(num_rows):
    fixed_eqp ="Equipe "
    for i in range (int(num_rows)):
        color= fake.color_name()
        name = fixed_eqp + str(color)
        get_db.add(Equipe(
            nomeEquipe= name
        ))
        get_db.commit()

def populate_membro(num_rows):
    team = choice(get_db.query(Equipe).all())
    team_id=  team.codigo
    f = choice(get_db.query(Funcionario).all())
    f_id = f.codigo
    for i in range(int(num_rows)):
        get_db.add(Membro(
            codEquipe_id= team_id,
            codFuncionario_id= f_id
        ))
        get_db.commit()

def populate_projeto(num_rows):
    cont = len(get_db.query(Projeto).all())
    fixed_proj = 'Projeto'
    for i in range(int (num_rows)):
        cont+=1
        last_character = cont
        description = fixed_proj + str(last_character)
        start_date = fake.date_between(start_date='-1y', end_date='today')
        end_date = fake.date_between(start_date=start_date, end_date='+1y')
        con'cl'usion_date = fake.date_between(start_date=start_date, end_date=end_date)
        status_options = ["Em andamento", "Concluído"]
        status = fake.random_element(status_options)
        get_db.add(Projeto(
            descricao=description,
            dataInicio=start_date,
            dataFim= end_date,
            situacao=status,
            dataConclusao=conclusion_date
        ))
        get_db.commit()
    for p in get_db.query(Projeto):
        if p.depto is None:
            departamento = choice(get_db.query(Departamento).all())
            p.depto = departamento
            p.depto_id= departamento.codigo
            get_db.commit()
        if p.responsavel is None:        
            responsavel = choice(get_db.query(Funcionario).all())
            p.responsavel_id = responsavel.codigo
            get_db.commit()
        if p.equipe is None:
            equipe = choice(get_db.query(Equipe).all())
            p.equipe=equipe
            p.equipe_id= equipe.codigo
            get_db.commit()

def populate_atividade(num_rows):
    cont = len(get_db.query(Atividade).all())
    fixed_atv="Atividade"
    for i in range(int(num_rows)):
        cont+=1
        last_character = cont
        description = fixed_atv + str(last_character)
        start_date = fake.date_between(start_date='-1y', end_date='today')
        end_date = fake.date_between(start_date=start_date, end_date='+1y')
        conclusion_date = fake.date_between(start_date=start_date, end_date=end_date)
        status_options = ["Em andamento", "Concluído"]
        status = fake.random_element(status_options)
        get_db.add(Atividade(
            descricao=description,
            dataInicio=start_date,
            dataFim=end_date,
            situacao=status,
            dataConclusao=conclusion_date
        ))
        get_db.commit()

def populate_atividadeMembro(num_rows):
    for i in range (int(num_rows)):
        m_id = choice(get_db.query(Membro).all()).codigo
        a_id = choice(get_db.query(Atividade).all()).codigo
        if not get_db.query(AtividadeMembro).all():
            get_db.add(AtividadeMembro(
                codAtividade=a_id,
                codMembro=m_id
            ))
            get_db.commit()
        else:
            for am in get_db.query(AtividadeMembro).all():
                m_id = choice(get_db.query(Membro).all()).codigo
                a_id = choice(get_db.query(Atividade).all()).codigo
                if (am.codAtividade != a_id and am.codMembro != m_id):
                    if(am.codAtividade is None):
                        get_db.add(AtividadeMembro(
                            codAtividade=a_id,
                            codMembro=m_id
                        ))
            get_db.commit()


def populate_atividadeProjeto(num_rows):
    for i in range (int(num_rows)):
        p_id = choice(get_db.query(Projeto).all()).codigo
        a_id = choice(get_db.query(Atividade).all()).codigo
        if not get_db.query(AtividadeProjeto).all():
            get_db.add(AtividadeProjeto(
                codAtividade=a_id,
                codProjeto=p_id
            ))
        else:
            for ap in get_db.query(AtividadeProjeto).all():
                p_id = choice(get_db.query(Projeto).all()).codigo
                a_id = choice(get_db.query(Atividade).all()).codigo
                if (ap.codAtividade != a_id and ap.codProjeto != p_id):
                    if(ap.codAtividade is None):
                        get_db.add(AtividadeProjeto(
                            codAtividade=a_id,
                            codProjeto=p_id 
                        ))
        get_db.commit()

if __name__ == '__main__':
    num_rows = 4 # alterar aqui caso deseje mais itens nas colunas
    populate_funcionario(num_rows)
    populate_departamento(num_rows)
    populate_equipe(num_rows)
    populate_membro(num_rows)
    populate_projeto(num_rows)
    populate_atividade(num_rows)
    populate_atividadeMembro(num_rows)
    populate_atividadeProjeto(num_rows)