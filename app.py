from flask import Flask, render_template, url_for, request, flash, session, redirect
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from models import User
import sqlite3
from database import obter_conexao
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = 'guilherme'

login_manager = LoginManager()
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
        ja_existe = conexao.execute(
            "SELECT * FROM users WHERE email = ?", (email,)).fetchone()

        if ja_existe:
            flash("Usuário já cadastrado!", category='error')
        else:
            senha_hash = generate_password_hash(senha)
            conexao.execute(
                "INSERT INTO users(email, senha) VALUES (?, ?)", (email, senha_hash))
            conexao.commit()
            flash("Cadastro realizado com sucesso!", category='success')

        conexao.close()
        return redirect(url_for('login'))

    return render_template('cadastro.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']

        conexao = obter_conexao()
        sql = "SELECT * FROM users WHERE email = ?"
        resultado = conexao.execute(sql, (email,)).fetchone()
        conexao.close()

        if resultado and check_password_hash(resultado['senha'], senha):
            user = User(nome=resultado['email'], senha=senha)
            user.id = resultado['id'] 
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
    return render_template('dashboard.html', lista_usuarios=User.all())




@app.route('/buscar', methods=['POST'])
@login_required
def buscar():
    termo = request.form.get('termo')
    if not termo:
        flash("Digite um e-mail para buscar.", category='error')
        return redirect(url_for('dash'))

    resultados = User.find_email(termo)
    return render_template('dashboard.html', lista_usuarios=resultados)

@app.route('/adicionar_atividade', methods=['GET', 'POST'])
@login_required
def cadastrar_atividade():
    if request.method == "POST":
        nome_atividade = request.form.get('nome_atividade')
        descricao_atividade = request.form.get('descricao_atividade')
        data_atividade = request.form.get('data_atividade')

        if not nome_atividade or not descricao_atividade or not data_atividade:
            flash("Preencha todos os campos!", category='error')
            return redirect(url_for('cadastrar_atividade'))

        conexao = obter_conexao()
        conexao.execute("""
            INSERT INTO atividades (nome_atividade, descricao_atividade, data_atividade, user_id)
            VALUES (?, ?, ?, ?)""", (nome_atividade, descricao_atividade, data_atividade, current_user.id))
        conexao.commit()
        conexao.close()

        flash("Atividade cadastrada com sucesso!", category='success')
        return redirect(url_for('dash'))


    return render_template('cadastrar_atividade.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/delete', methods=['POST'])
@login_required
def delete():
    email = request.form['user']
    if email != current_user.nome:
        User.delete(email)
        flash(f"Usuário {email} deletado com sucesso.", category='success')
    else:
        flash("Você não pode deletar a si mesmo!", category='error')

    return redirect(url_for('dash'))


@app.route('/minhas_atividades')
@login_required
def minhas_atividades():
    conexao = obter_conexao()
    atividades = conexao.execute("""
        SELECT ati_id, nome_atividade, descricao_atividade, data_atividade
        FROM atividades
        WHERE user_id = ?
    """, (current_user.id,)).fetchall()
    conexao.close()

    return render_template('minhas_atividades.html', atividades=atividades)


if __name__ == '__main__':
    app.run(debug=True)
