from flask import *
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    if request.method == "POST":
        return redirect(url_for('login'))

    return render_template('cadastro.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/dashboard')
def dash():
    return render_template('dash.html')

@app.route('/logout')
def logout():
    return render_template('index.html')


