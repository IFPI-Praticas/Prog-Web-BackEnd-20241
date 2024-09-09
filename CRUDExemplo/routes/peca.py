from flask import Blueprint, render_template, request, redirect
from database import db
from models import Peca

peca_route = Blueprint('peca', __name__)

@peca_route.route('/')
def listagem_pecas():
    lista_pecas = Peca.query.all()
    return render_template('listagem_pecas.html', lista=lista_pecas)
