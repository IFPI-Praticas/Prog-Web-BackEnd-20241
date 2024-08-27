from database import db

class Peca(db.Model):
    __tablename__ = 'pecas'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    quantidade = db.Column(db.Integer)
    valor = db.Column(db.Float)

    def __init__(self, nome, quantidade, valor):
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor

    def __repr__(self) -> str:
        return "<Peca {}>".format(self.nome)