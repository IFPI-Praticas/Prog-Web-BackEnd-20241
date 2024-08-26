from flask import Flask, render_template, redirect, request, flash
from database import db
from flask_migrate import Migrate
from models import Peca

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

if __name__ == '__main__':
    app.run()