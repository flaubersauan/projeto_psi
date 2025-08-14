from flask_login import UserMixin

from flask import session, flash

from database import obter_conexao

class User(UserMixin):
    email: str
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    @classmethod
    def get(cls, user_id):
        conexao = obter_conexao()
        sql = "SELECT * FROM users WHERE id = ?"
        resultado = conexao.execute(sql, (user_id,)).fetchone()
        conexao.close()

        if resultado:
            user = User(nome=resultado['email'], senha=resultado['senha'])
            user.id = resultado['id'] 
            return user
        return None
    
    @classmethod
    def all(cls):

        conexao = obter_conexao()
        sql = "SELECT email FROM users"
        resultado = conexao.execute(sql).fetchall()
        lista_emails = []
        for linha in resultado:
            lista_emails.append(linha["email"])
        return lista_emails
    
    @classmethod

    def find_email(cls, email):
        conexao = obter_conexao()
        sql = "SELECT email FROM users WHERE email LIKE ?"
        resultado = conexao.execute(sql, ('%' + email + '%',)).fetchall()
        conexao.close()
        lista_emails = []
        for linha in resultado:
            lista_emails.append(linha["email"])
        return lista_emails

    def save(self):
        pass





    @classmethod


    def delete(cls, email):


        conexao = obter_conexao()


        conexao.execute("DELETE FROM users WHERE email = ?", (email,))


        conexao.commit()


        conexao.close()

