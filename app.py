from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dados simulados (em produção, use banco de dados)
estudantes = []
instituicoes = []

@app.route('/')
def index():
    return render_template('index.html', estudantes=estudantes, instituicoes=instituicoes)

@app.route('/cadastrar_estudante', methods=['GET', 'POST'])
def cadastrar_estudante():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        estudantes.append({'nome': nome, 'email': email})
        return redirect(url_for('index'))
    return render_template('cadastrar_estudante.html')

@app.route('/cadastrar_instituicao', methods=['GET', 'POST'])
def cadastrar_instituicao():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        instituicoes.append({'nome': nome, 'descricao': descricao})
        return redirect(url_for('index'))
    return render_template('cadastrar_instituicao.html')

@app.route('/planos')
def planos():
    valor = 1500
    descricao = "Ao aderir ao plano no valor de R$ 1.500,00, sua instituição receberá voluntários capacitados para atuar diretamente na casa de acolhimento, além de acesso a conteúdos exclusivos e rede de apoio."
    return render_template('planos.html', valor=valor, descricao=descricao)

if __name__ == "__main__":
    app.run(debug=True)
