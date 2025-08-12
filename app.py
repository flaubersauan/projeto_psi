from flask import Flask, render_template
from flask import url_for, request, flash

from flask_login import LoginManager, login_required
from flask_login import login_user, logout_user, current_user
from flask import session, redirect

from models import User

import sqlite3
from database import obter_conexao
from models import db

login_manager = LoginManager() 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seu_banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'caladoSEUinUTIL'
db.init_app(app)
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

@app.route('/sugestao',methods=['GET', 'POST'])
def sugerir():
    return render_template('sugestao.html')

@app.route('/dash')
@login_required
def dash():
    return render_template('dash.html', lista_usuarios=User.all())

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
