from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html', tel='(86)999495137', 
                           email='rogerio.sousa@ifpi.edu.br')

#@app.route('/usuario', defaults={"nome":"usuário comum"})
#@app.route('/usuario/<nome>')
#def usuario(nome):
#    return nome

@app.route('/semestre/<int:x>')
def semestre(x):
    return "Estamos no semestre " + str(x)

@app.route('/somar/<int:x>/<int:y>')
def somar(x,y):
    dados = {'n1':x, 'n2':y, 'soma':x+y}
    return render_template('soma.html', dados=dados)

@app.route('/perfil/<usuario>')
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)

@app.route('/dados')
def dados():
    return render_template('dados.html')

@app.route('/recebedados', methods=['POST'])
def recebedados():
    nome = request.form['nome']
    email = request.form.get('email')
    estado = request.form.get('estado')
    formacao = request.form.get('formacao')
    modalidades = request.form.getlist('modalidades')
    
    return "{} - {} - {} - {} - {}".format(nome,email,estado, formacao, modalidades)

@app.route('/verificaidade/<int:idade>') # localhost:5000/verificaridade/78
def verificaidade(idade):
    return render_template('verificaridade.html', idade=idade)

@app.route('/login')
def telalogin():
    return render_template('login.html')

@app.route('/verificarlogin', methods=['POST'])
def verificarlogin():
    usuario = request.form['login']
    senha = request.form['senha']

    if usuario == 'admin' and senha == '12345':
        return "Login efetuado com sucesso!"
    else:
        return "Erro de autenticação!"

@app.route('/usuario/<user>')
def usuario(user):
    esportes = ['Futebol', 'Judô','Basquete','Natação']
    # print(esportes)
    return render_template('principal.html', user=user, esportes=esportes)

if __name__ == '__main__':
    app.run()