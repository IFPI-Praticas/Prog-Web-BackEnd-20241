from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from models import Usuario

usuario_route = Blueprint('usuario', __name__)

@usuario_route.route('/')
def listagem_usuarios():
    lista_usuarios = Usuario.query.all()
    return render_template('listar_usuarios.html', lista=lista_usuarios)

@usuario_route.route('/cadastrar', methods=['GET','POST'])
def cadastrar_usuario():
    if request.method == 'GET':
        return render_template('cadastrar_usuario.html')
    
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        u = Usuario(nome, email, senha)

        db.session.add(u)
        db.session.commit()
        
        return redirect(url_for('usuario.listagem_usuarios'))
    
@usuario_route.route('/editar/<int:id_usuario>')
def editar(id_usuario):

    user = Usuario.query.get(id_usuario)

    return render_template('editar_usuario.html', dados_usuario=user)

@usuario_route.route('/editar_enviar', methods=['POST'])
def editar_enviar():
    id_usuario = request.form['id_usuario']
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    user = Usuario.query.get(id_usuario)
    user.nome = nome
    user.email = email
    user.senha = senha

    db.session.add(user)
    db.session.commit()

    flash('Usuário editado com sucesso!', 'success')
    return redirect(url_for('usuario.listagem_usuarios'))

@usuario_route.route('/excluir/<int:id_usuario>')
def excluir(id_usuario):
    user = Usuario.query.get(id_usuario)

    db.session.delete(user)
    db.session.commit()

    flash('Usuário excluído com sucesso!','danger')
    return redirect(url_for('usuario.listagem_usuarios'))