from flask import Flask, render_template, request, redirect, Blueprint
from database import db
from flask_migrate import Migrate
from models import Peca, Usuario, Pedido
from routes.home import home_route
from routes.peca import peca_route

app = Flask(__name__)

conexao = "sqlite:///meubanco.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(home_route)
app.register_blueprint(peca_route, url_prefix='/pecas')

'''
    Usuários
'''
@app.route('/usuarios')
def listagem_usuarios():
    lista_usuarios = Usuario.query.all()
    return render_template('listar_usuarios.html', lista=lista_usuarios)

@app.route('/usuario/cadastrar', methods=['GET','POST'])
def cadastrar_usuario():
    if request.method == 'GET':
        return render_template('cadastrar_usuario.html')
    
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']

        u = Usuario(nome, email)

        db.session.add(u)
        db.session.commit()
        
        return redirect('/usuarios')

'''
    Pedidos
'''

if __name__ == '__main__':
    app.run()