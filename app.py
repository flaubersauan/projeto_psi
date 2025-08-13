from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seu_banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'caladoSEUinUTIL'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # redireciona para login se não estiver autenticado

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

        if User.query.filter_by(email=email).first():
            flash("Usuário já cadastrado!", category='error')
        else:
            senha_hash = generate_password_hash(senha)
            novo_user = User(email=email, senha=senha_hash)
            db.session.add(novo_user)
            db.session.commit()
            flash("Cadastro realizado com sucesso!", category='success')
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.senha, senha):
            login_user(user)
            flash('Login realizado com sucesso!', category='success')
            return redirect(url_for('dash'))
        else:
            flash('Email ou senha inválidos.', category='error')

    return render_template('login.html')

@app.route('/dash')
@login_required
def dash():
    usuarios = User.all()
    return render_template('dash.html', lista_usuarios=usuarios)

@app.route('/buscar', methods=['POST'])
@login_required
def buscar():
    termo = request.form.get('termo', '')
    if termo:
        usuarios_filtrados = User.query.filter(User.email.contains(termo)).all()
    else:
        usuarios_filtrados = User.all()
    return render_template('dash.html', lista_usuarios=usuarios_filtrados)

@app.route('/delete', methods=['POST'])
@login_required
def delete():
    email_usuario = request.form.get('user_email')
    if email_usuario:
        usuario = User.query.filter_by(email=email_usuario).first()
        if usuario:
            if usuario.id == current_user.id:
                flash("Você não pode deletar seu próprio usuário!", category='error')
            else:
                db.session.delete(usuario)
                db.session.commit()
                flash(f"Usuário {email_usuario} deletado com sucesso!", category='success')
        else:
            flash("Usuário não encontrado!", category='error')
    else:
        flash("Email do usuário não informado.", category='error')

    return redirect(url_for('dash'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/sugerir')
@login_required
def sugerir():
    return render_template('sugestao.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas se não existirem
    app.run(debug=True)

