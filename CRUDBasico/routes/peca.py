from flask import Blueprint, render_template, request, redirect, url_for
from database import db
from models import Peca

peca_route = Blueprint('peca', __name__)

@peca_route.route('/')
def index():
    dados = Peca.query.all()
    return render_template('lista_pecas.html', lista=dados)

@peca_route.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'GET':
        return render_template('cadastrar_peca.html')
    
    if request.method == 'POST':
        nome = request.form['nome']
        quantidade = request.form['quantidade']
        valor = request.form['valor']

        nova_peca = Peca(nome, quantidade, valor)
        db.session.add(nova_peca)
        db.session.commit()

        return redirect(url_for('peca.index'))

@peca_route.route('/editar/<int:peca_id>', methods=['GET', 'POST'])
def editar(peca_id):
    if request.method == 'GET':
        peca = Peca.query.get(peca_id)
        return render_template('editar_peca.html', peca=peca)
    
    if request.method == 'POST':
        peca_id = int(request.form['id_peca'])
    
        peca = Peca.query.get(peca_id)

        peca.nome = request.form['nome']
        peca.quantidade = request.form['quantidade']
        peca.valor = request.form['valor']

        db.session.commit()
    
        return redirect(url_for('peca.index'))


@peca_route.route('/excluir/<int:peca_id>')
def excluir(peca_id):
    peca = Peca.query.get(peca_id)

    db.session.delete(peca)
    db.session.commit()
    
    return redirect(url_for('peca.index'))