from flask import Flask, render_template, redirect, request, flash
from database import db
from flask_migrate import Migrate
from models import Peca, Usuario, Pedido
from datetime import date

app = Flask(__name__)

app.secret_key = 'minha_chave_secreta'

conexao = "sqlite:///database.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app,db)

@app.route('/')
def index():
    dados = Peca.query.all()
    return render_template('index.html', lista=dados)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')

@app.route('/cadastrar_enviar', methods=['POST'])
def cadastrar_enviar():
    nome = request.form['nome']
    quantidade = request.form['quantidade']
    valor = request.form['valor']

    nova_peca = Peca(nome, quantidade, valor)
    db.session.add(nova_peca)
    db.session.commit()

    flash('Cadastrado com sucesso!')

    return redirect('/')


@app.route('/editar/<int:peca_id>')
def editar(peca_id):
    peca = Peca.query.get(peca_id)
    return render_template('editar.html', peca=peca)

@app.route('/editar_enviar', methods=['POST'])
def editar_enviar():
    peca_id = int(request.form['id_peca'])
    
    peca = Peca.query.get(peca_id)

    peca.nome = request.form['nome']
    peca.quantidade = request.form['quantidade']
    peca.valor = request.form['valor']

    db.session.commit()
    
    # adiciona uma mensagem de sucesso ao usuário
    flash('Cadastro editado com sucesso!')
    return redirect('/')


@app.route('/excluir/<int:peca_id>')
def excluir(peca_id):
    peca = Peca.query.get(peca_id)

    db.session.delete(peca)
    db.session.commit()
    
    flash('Item excluído com sucesso!')
    return redirect('/')

## Usuarios
@app.route('/usuarios')
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuario_listar.html', lista=usuarios)

@app.route('/usuarios/cadastrar')
def cadastrar_usuario():
    return render_template('usuario_cadastrar.html')

@app.route('/usuarios/cadastrar_enviar', methods=['POST'])
def cadastrar_usuario_enviar():
    nome = request.form['nome']
    email = request.form['email']

    novo_usuario = Usuario(nome, email)
    db.session.add(novo_usuario)
    db.session.commit()

    flash('Cadastrado com sucesso!')

    return redirect('/usuarios')


@app.route('/usuario/editar/<int:usuario_id>')
def editar_usuario(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    return render_template('usuario_editar.html', usuario=usuario)

@app.route('/usuario/editar_enviar', methods=['POST'])
def editar_usuario_enviar():
    usuario_id = int(request.form['id_usuario'])
    
    usuario = Usuario.query.get(usuario_id)

    usuario.nome = request.form['nome']
    usuario.email = request.form['email']

    db.session.commit()
    
    # adiciona uma mensagem de sucesso ao usuário
    flash('Cadastro editado com sucesso!')
    return redirect('/usuarios')


@app.route('/usuario/excluir/<int:usuario_id>')
def excluir_usuario(usuario_id):
    usuario = Usuario.query.get(usuario_id)

    db.session.delete(usuario)
    db.session.commit()
    
    flash('Item excluído com sucesso!')
    return redirect('/usuarios')


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