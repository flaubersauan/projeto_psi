from flask import *
from flask_login import login_user, logout_user, login_manager, login_required, LoginManager
from models import User
from database import obter_conexao

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = 'vc está sendo perspicaz'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/register')
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

    return render_template('cadastro.html')

@app.route('/login')
def login():
    return render_template('login.html')

@login_required
@app.route('/dashboard')
def dash():
    return render_template('dash.html')

@login_required
@app.route('/logout')
def logout():
    logout_user()
    return render_template('index.html')

# Sauan guaxinim