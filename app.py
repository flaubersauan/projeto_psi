from flask import Flask, render_template, url_for, request, flash, redirect
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from models import User
from database import obter_conexao
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = 'guilherme'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        conexao = obter_conexao()
        existente = conexao.execute(
            "SELECT id FROM users WHERE email = ?", (email,)
        ).fetchone()

        if existente:
            flash("E-mail já cadastrado!", "error")
            conexao.close()
            return redirect(url_for("register"))

        conexao.execute(
            "INSERT INTO users (email, senha) VALUES (?, ?)",
            (email, senha)  # Ideal: usar hash
        )
        conexao.commit()
        conexao.close()

        flash("Usuário registrado com sucesso!", "success")
        return redirect(url_for("login"))

    return render_template("cadastro.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']

        conexao = obter_conexao()
        resultado = conexao.execute(
            "SELECT * FROM users WHERE email = ?", (email,)
        ).fetchone()
        conexao.close()

        if resultado and resultado["senha"] == senha:  # Ideal: usar hash
            user = User(
                id=resultado['id'],
                email=resultado['email'],
                senha=resultado['senha']
            )
            login_user(user)
            flash("Login realizado com sucesso!", "success")
            return redirect(url_for("dash"))
        else:
            flash("Email ou senha incorretos!", "error")

    return render_template("login.html")


@app.route('/sugestao', methods=['GET', 'POST'])
def sugerir():
    return render_template('sugestao.html')


@app.route('/dash')
@login_required
def dash():
    return render_template('dashboard.html')


@app.route('/adicionar_atividade', methods=['GET', 'POST'])
@login_required
def cadastrar_atividade():
    conexao = obter_conexao()

    # Cria a tabela com user_id vinculado ao usuário
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS atividades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)
    conexao.commit()

    if request.method == "POST":
        nome_atividade = request.form.get('nome')
        descricao = request.form.get('descricao')

        if not nome_atividade:
            flash("O nome da atividade é obrigatório.", category='error')
        else:
            conexao.execute(
                "INSERT INTO atividades (nome, descricao, user_id) VALUES (?, ?, ?)",
                (nome_atividade, descricao, current_user.id)
            )
            conexao.commit()
            flash("Atividade cadastrada com sucesso!", category='success')

    # Filtra atividades do usuário logado
    atividades = conexao.execute(
        "SELECT * FROM atividades WHERE user_id = ?",
        (current_user.id,)
    ).fetchall()

    conexao.close()
    return render_template('cadastrar_atividade.html', atividades=atividades)


@app.route('/delete_atividade', methods=['POST'])
@login_required
def delete_atividade():
    id_atividade = request.form.get('atividade_id')
    conexao = obter_conexao()
    conexao.execute(
        "DELETE FROM atividades WHERE id = ? AND user_id = ?",
        (id_atividade, current_user.id)
    )
    conexao.commit()
    conexao.close()
    flash("Atividade removida com sucesso!", category='success')
    return redirect(url_for('cadastrar_atividade'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('componentes/erro.html', codigo=404, mensagem="Página não encontrada"), 404

@app.errorhandler(500)
def erro_interno(e):
    return render_template('componentes/erro.html', codigo=500, mensagem="Erro interno do servidor"), 500


if __name__ == '__main__':
    app.run(debug=True)
