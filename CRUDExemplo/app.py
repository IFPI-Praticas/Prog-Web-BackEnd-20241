from flask import Flask, render_template, request, redirect
from database import db
from flask_migrate import Migrate
from models import Peca

app = Flask(__name__)

conexao = "sqlite:///meubanco.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    lista_pecas = Peca.query.all()
    return render_template('index.html', lista=lista_pecas)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')

@app.route('/cadastrar_enviar', methods=['POST'])
def cadastrar_enviar():
    nome = request.form['nome']
    quantidade = request.form['quantidade']
    valor = request.form['valor']

    p = Peca(nome, quantidade, valor)

    db.session.add(p)
    db.session.commit()
    
    return redirect('/')

@app.route('/editar/<int:id_peca>')
def editar(id_peca):

    p = Peca.query.get(id_peca)

    return render_template('editar.html', dados_peca=p)

@app.route('/editar_enviar', methods=['POST'])
def editar_enviar():
    id_peca = request.form['id_peca']
    nome = request.form['nome']
    quantidade = request.form['quantidade']
    valor = request.form['valor']

    p = Peca.query.get(id_peca)
    p.nome = nome
    p.quantidade = quantidade
    p.valor = valor

    db.session.add(p)
    db.session.commit()

    return redirect('/')

@app.route('/excluir/<int:id_peca>')
def excluir(id_peca):
    p = Peca.query.get(id_peca)

    db.session.delete(p)
    db.session.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run()