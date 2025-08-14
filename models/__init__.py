from flask_login import UserMixin
from database import obter_conexao

class User(UserMixin):
    def __init__(self, id, email, senha):
        self.id = id           # id numérico do banco
        self.email = email
        self.senha = senha

    @classmethod
    def get(cls, user_id):
        conexao = obter_conexao()
        sql = "SELECT * FROM users WHERE id = ?"
        resultado = conexao.execute(sql, (user_id,)).fetchone()
        conexao.close()

        if resultado is None:
            return None

        # Cria o objeto User já com id numérico
        return cls(
            id=resultado['id'],
            email=resultado['email'],
            senha=resultado['senha']
        )

    @classmethod
    def all(cls):
        conexao = obter_conexao()
        sql = "SELECT id, email FROM users"
        resultado = conexao.execute(sql).fetchall()
        conexao.close()

        return [{"id": linha["id"], "email": linha["email"]} for linha in resultado]

    @classmethod
    def delete(cls, user_id):
        conexao = obter_conexao()
        conexao.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conexao.commit()
        conexao.close()

    def save(self):
        conexao = obter_conexao()
        conexao.execute(
            "INSERT INTO users (email, senha) VALUES (?, ?)",
            (self.email, self.senha)
        )
        conexao.commit()
        conexao.close()
