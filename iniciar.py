import sqlite3 
from database import obter_conexao

BANCO = 'schema.sql'

conexao = obter_conexao()

with open(BANCO) as f:
    conexao.executescript(f.read())
    
conexao.close()

