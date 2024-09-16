from flask import Flask, render_template, redirect, request, flash
from utils import db, lm
from flask_migrate import Migrate
from models import Peca, Usuario, Pedido
from datetime import date

from routes.home import home_route
from routes.peca import peca_route
from routes.usuario import usuario_route

app = Flask(__name__)

app.secret_key = 'minha_chave_secreta'

conexao = "sqlite:///database.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
lm.init_app(app)
migrate = Migrate(app,db)

app.register_blueprint(home_route)
app.register_blueprint(peca_route, url_prefix='/peca')
app.register_blueprint(usuario_route, url_prefix='/usuario')

@app.errorhandler(401)
def acesso_negado(e):
    # note that we set the 404 status explicitly
    return render_template('acesso_negado.html'), 404

## Pedidos
@app.route('/pedido/create', methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('pedidos_create.html')

    if request.method == 'POST':
        id_usuario = request.form['id_usuario']
        id_peca = request.form['id_peca']
        data = date.today()

        pedido = Pedido(id_usuario, id_peca, data)
        db.session.add(pedido)
        db.session.commit()

        flash('Pedido criado com sucesso!')
        return redirect('/')
    
@app.route('/pedidos', methods=['GET'])
def listar_pedidos():
    pedidos = Pedido.query.all()
    return render_template('pedidos_lista.html', pedidos=pedidos)

if __name__ == '__main__':
    app.run()