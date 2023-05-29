import pyodbc

def session():
    conn = pyodbc.connect('DRIVER={PostgreSQL ANSI(x64)};Server=localhost;Port=5400;Database=empresa_db;User ID=root;Password=password;String Types=Unicode')

    return conn
