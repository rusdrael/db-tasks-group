# Tarefa 03 - Conexões ODBC e ORM

[Link para a tarefa](https://docs.google.com/document/d/1pEhJvmaZb_QBZvUhxBW_p1bHIv3mayhIpQIwG9OLsj4/edit)

## Respostas das questões

- [Questão 02](/tarefas/t03/app/api/routes/odbc.py)
- [Questão 03.b](/tarefas/t03/app/api/routes/atividades.py)
- [Questão 04](/tarefas/t03/app/database/populate.py)
- [Questão 05](/tarefas/t03/app/database/relatorio.py)
- **Questão 07:** Inidices presentes nos models da [questão 05](/tarefas/t03/app/database/relatorio.py)
## Resumo sobre ORM
<p align = justify>
Object Relational Mapper (ORM) é uma técnica de programação que permite mapear objetos de uma linguagem de programação para estruturas de dados em um banco de dados relacional. O objetivo do ORM é facilitar a interação entre um aplicativo orientado a objetos e um banco de dados relacional, fornecendo uma camada de abstração que permite manipular os dados do banco de dados usando objetos e métodos da linguagem de programação, utilizado para facilitar a interação entre o aplicativo e o banco de dados, simplificanco o desenvolvimento, melhorando a produtividade e aumentando a legibilidade do código.
</p>

## ORM escolhido - SQLAlchemy
<p align = justify>
SQLAlchemy é uma biblioteca popular de mapeamento objeto-relacional (ORM) para Python. Ela fornece uma interface de programação de alto nível para interagir com bancos de dados relacionais usando objetos Python em vez de escrever consultas SQL diretamente. O SQLAlchemy permite que os desenvolvedores escrevam código Python para manipular dados no banco de dados, abstraindo as complexidades do SQL subjacente. Ele oferece suporte a vários bancos de dados, incluindo MySQL, PostgreSQL, SQLite, Oracle, entre outros. Uma das principais características do SQLAlchemy é seu recurso de mapeamento objeto-relacional, que permite que os desenvolvedores definam classes Python que representam tabelas no banco de dados. Essas classes são chamadas de classes de modelo ou classes de tabela. O SQLAlchemy mapeia automaticamente as propriedades dessas classes para as colunas correspondentes no banco de dados e fornece métodos para realizar operações de leitura, gravação, atualização e exclusão nessas tabelas.

Além de tudo isso, ele também possui recursos avançados, como relacionamentos entre tabelas, consultas complexas, controle transacional, geração de esquemas, entre outros. Os desenvolvedores escrevem consultas intuitivas semelhantes ao SQL mas com o poder do Python. O SQLAlchemy nos polpa trabalho, a biblioteca cuida das operações do banca de dados, dessa forma, os desenvolvedores podem focar mais no código. É amplamente utilizado em projetos Python de todos os tamanhos, desde pequenas aplicações até sistemas complexos e de grande escala. Com o SQLAlchemy, os desenvolvedores podem criar aplicativos robustos e eficientes, facilitando o trabalho com bancos de dados relacionais no ecossistema Python.
</p>

##  Como funciona o ORM escolhido
- O SQLAlchemy é uma biblioteca ORM para Python, que facilita a interação com bancos de dados relacionais.
- Ele utiliza classes Python para representar tabelas do banco de dados e objetos relacionados.
- A configuração inicial envolve fornecer detalhes da conexão, como tipo de banco de dados, host e credenciais.
- As classes Python são mapeadas para tabelas usando metadados e decoradores.
- As consultas são escritas usando SQLAlchemy Query Language (SQLAlchemy ORM).
- As sessões são utilizadas para interagir com o banco de dados, controlar transações e executar consultas.
- As alterações em objetos são rastreadas e aplicadas no banco de dados quando a sessão é commitada.
- O SQLAlchemy oferece recursos avançados como suporte a relacionamentos, cache de consultas e migração de banco de dados.
- Sua documentação oficial é uma excelente fonte de referência para explorar todos os recursos disponíveis. 
