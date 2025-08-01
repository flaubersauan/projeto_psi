from flask import Flask, render_template
from flask import url_for, request, flash

from flask_login import LoginManager, login_required
from flask_login import login_user, logout_user, current_user
from flask import session, redirect

from modelos import User

import sqlite3
from database import obter_conexao

login_manager = LoginManager() 
app = Flask(__name__)
app.secret_key = 'guilherme'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']

        conexao = obter_conexao()
        ja_existe = conexao.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()

        if ja_existe:
            flash("Usuário já cadastrado!", category='error')
        else:
            conexao.execute("INSERT INTO users(email, senha) VALUES (?, ?)", (email, senha))
            conexao.commit()
            flash("Cadastro realizado com sucesso!", category='success')

        conexao.close()
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']

        conexao = obter_conexao()
        sql = "SELECT * FROM users WHERE email = ?"
        resultado = conexao.execute(sql, (email,) ).fetchone()
        conexao.close()

        if resultado and resultado['senha'] == senha:
            user = User(nome=email, senha=senha)
            user.id = email
            login_user(user)
            flash('Login realizado com sucesso!', category='success')
            return redirect(url_for('dash'))
        else:
            flash('Email ou senha inválidos.', category='error')

    return render_template('login.html')

@app.route('/dash')
@login_required
def dash():
    return render_template('dash.html', lista_usuarios=User.all())

@app.route('/buscar', methods=['POST'])
@login_required
def buscar():
    termo = request.form.get('termo')
    if not termo:
        flash("Digite um e-mail para buscar.", category='error')
        return redirect(url_for('dash'))

    resultados = User.find_email(termo)
    return render_template('dash.html', lista_usuarios=resultados)

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/delete', methods=['POST'])
def delete():
    email = request.form['user']
    if email != current_user.nome: 
        User.delete(email)
        flash(f"Usuário {email} deletado com sucesso.", category='success')
    else:
        flash("Você não pode deletar a si mesmo!", category='error')
    return redirect(url_for('dash'))
