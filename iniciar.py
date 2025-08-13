import sqlite3 
from app import obter_conexao

BANCO = 'schema.sql'

conexao = obter_conexao()

with open(BANCO) as f:
    conexao.executescript(f.read())
    
conexao.close()