from flask import Flask, render_template, url_for, request, flash, redirect
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from models import User
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
            "SELECT * FROM users WHERE email = ?", (email,)
        ).fetchone()

        if ja_existe:
            flash("Usuário já cadastrado!", category='error')
        else:
            senha_hash = generate_password_hash(senha)
            conexao.execute(
                "INSERT INTO users(email, senha) VALUES (?, ?)",
                (email, senha_hash)
            )
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
        resultado = conexao.execute(
            "SELECT * FROM users WHERE email = ?", (email,)
        ).fetchone()
        conexao.close()

        if resultado and check_password_hash(resultado['senha'], senha):
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
    conexao = obter_conexao()

    
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS atividades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT
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
                "INSERT INTO atividades (nome, descricao) VALUES (?, ?)",
                (nome_atividade, descricao)
            )
            conexao.commit()
            flash("Atividade cadastrada com sucesso!", category='success')

    atividades = conexao.execute("SELECT * FROM atividades").fetchall()
    conexao.close()

    return render_template('cadastrar_atividade.html', atividades=atividades)


@app.route('/delete_atividade', methods=['POST'])
@login_required
def delete_atividade():
    id_atividade = request.form.get('atividade_id')
    conexao = obter_conexao()
    conexao.execute("DELETE FROM atividades WHERE id = ?", (id_atividade,))
    conexao.commit()
    conexao.close()
    flash("Atividade removida com sucesso!", category='success')
    return redirect(url_for('cadastrar_atividade'))


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



@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('componentes/erro.html', codigo=404, mensagem="Página não encontrada"), 404

@app.errorhandler(500)
def erro_interno(e):
    return render_template('componentes/erro.html', codigo=500, mensagem="Erro interno do servidor"), 500


if __name__ == '__main__':
    app.run(debug=True)
