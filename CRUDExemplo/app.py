from flask import Flask, render_template, request, redirect

app = Flask(__name__)

dados = [{'id': 0, 'nome': 'Bieleta', 'quantidade': 10, 'valor': 805.5},
         {'id': 1, 'nome': 'Coxim', 'quantidade': 16, 'valor': 1500.00}
         ]
@app.route('/')
def index():
    return render_template('index.html', lista=dados)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')

@app.route('/cadastrar_enviar', methods=['POST'])
def cadastrar_enviar():
    nome = request.form['nome']
    quantidade = request.form['quantidade']
    valor = request.form['valor']

    nova_peca = {
        'id': len(dados),
        'nome' : nome,
        'quantidade': quantidade,
        'valor': valor
    }

    dados.append(nova_peca)
    return redirect('/')

@app.route('/editar/<int:id_peca>')
def editar(id_peca):
    dados_peca = [peca for peca in dados if peca['id'] == id_peca][0]
    
    return render_template('editar.html', dados_peca=dados_peca)

@app.route('/editar_enviar', methods=['POST'])
def editar_enviar():
    id_peca = request.form['id_peca']
    nome = request.form['nome']
    quantidade = request.form['quantidade']
    valor = request.form['valor']


    dados_peca = [peca for peca in dados if peca['id'] == int(id_peca)][0]

    dados_peca['nome'] = nome
    dados_peca['quantidade'] = quantidade
    dados_peca['valor'] = valor

    return redirect('/')

if __name__ == '__main__':
    app.run()