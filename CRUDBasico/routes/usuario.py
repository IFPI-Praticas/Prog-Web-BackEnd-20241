from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils import db, lm
from models import Usuario
from flask_login import login_user, logout_user, login_required

usuario_route = Blueprint('usuario', __name__)

@usuario_route.route('/')
@login_required
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuario_listar.html', lista=usuarios)

@usuario_route.route('/cadastrar')
def cadastrar_usuario():
    return render_template('usuario_cadastrar.html')

@usuario_route.route('/cadastrar_enviar', methods=['POST'])
def cadastrar_usuario_enviar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    novo_usuario = Usuario(nome, email, senha)
    db.session.add(novo_usuario)
    db.session.commit()

    flash('Cadastrado com sucesso!')

    return redirect(url_for('usuario.listar_usuarios'))


@usuario_route.route('/editar/<int:usuario_id>')
def editar_usuario(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    return render_template('usuario_editar.html', usuario=usuario)

@usuario_route.route('/editar_enviar', methods=['POST'])
def editar_usuario_enviar():
    usuario_id = int(request.form['id_usuario'])
    
    usuario = Usuario.query.get(usuario_id)

    usuario.nome = request.form['nome']
    usuario.email = request.form['email']
    usuario.senha = request.form['antiga_senha']
    usuario.senha = request.form['nova_senha']

    db.session.commit()
    
    # adiciona uma mensagem de sucesso ao usuário
    flash('Cadastro editado com sucesso!')
    return redirect(url_for('usuario.listar_usuarios'))


@usuario_route.route('/excluir/<int:usuario_id>')
def excluir_usuario(usuario_id):
    usuario = Usuario.query.get(usuario_id)

    db.session.delete(usuario)
    db.session.commit()
    
    flash('Item excluído com sucesso!')
    return redirect(url_for('usuario.listar_usuarios'))

@lm.user_loader
def load_user(id):
    usuario = Usuario.query.filter_by(id=id).first()
    #usuario = Usuario.query.get(id)
    return usuario

@usuario_route.route('/autenticar', methods=['POST'])
def autenticar():
    email = request.form.get('email')
    senha = request.form.get('senha')
    usuario = Usuario.query.filter_by(email = email).first()
    if (usuario and (senha == usuario.senha)):
        login_user(usuario)
        return redirect(url_for('home.home'))
    else:
        flash('Dados incorretos')
        return redirect(url_for('home.home'))
    

@usuario_route.route('/login')
def login():
    return render_template('login.html')

@usuario_route.route('/logoff')
def logoff():
	logout_user()
	return redirect('/')

