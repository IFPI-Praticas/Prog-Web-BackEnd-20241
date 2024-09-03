from database import db

class Peca(db.Model):
    __tablename__ = 'pecas'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    quantidade = db.Column(db.Integer)
    valor = db.Column(db.Float)
    pedidos = db.relationship('Pedido', backref='peca')


    def __init__(self, nome, quantidade, valor):
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor

    def __repr__(self) -> str:
        return "<Peca {}>".format(self.nome)
    
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    pedidos = db.relationship('Pedido', backref='usuario')

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    def __repr__(self):
        return "<Usuario {}>".format(self.nome)

class Pedido(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    id_peca = db.Column(db.Integer, db.ForeignKey('pecas.id'))
    data = db.Column(db.Date)

    def __init__(self, id_usuario, id_peca, data):
        self.id_usuario = id_usuario
        self.id_peca = id_peca
        self.data = data
    
    def __repr__(self):
        return "<Pedido {} - {} - {}>".format(self.usuario.nome, self.peca.nome, self.data)