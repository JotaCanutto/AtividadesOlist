from flask import Flask, render_template, request
from listagem import *
from historico import *

app = Flask(__name__)

titulo_app = 'Marketplaces'

@app.route('/')
def index():
    cadastro_marketplace = {'nome': 'Cadastrar Marketplace', 'rota': '/form_marketplace'}
    listagem_marketplaces = {'nome': 'Listar Marketplaces', 'rota': '/listagem_marketplaces'}
    listagem_categorias = {'nome': 'Listar Categorias', 'rota': '/listagem_categorias'}
    listagem_subcategorias = {'nome': 'Listar Subcategorias', 'rota': '/listagem_subcategorias'}
    lista = [cadastro_marketplace, listagem_marketplaces, listagem_categorias, listagem_subcategorias]
    return render_template('index.html', nome=titulo_app, lista=lista)

@app.route('/form_marketplace')
def form_marketplace():
    return render_template('cadastrar_marketplace.html', nome=titulo_app)

@app.route('/cadastrar_marketplace')
def cadastrar_marketplace():
    nome_marketplace = request.args.get('marketplace')
    gravar_marketplaces(nome_marketplace)
    return f'Marketplace cadastrado com sucesso!'

# @app.route('/listagem_marketplaces')
# def listagem_marketplaces():
#     texto = exibir_marketplaces()
#     return render_template('listagem_marketplaces.html', nome=titulo_app, listagem=texto)

@app.route('/listagem_marketplaces')
def listagem_marketplaces():
    lista = ler_marketplaces()
    return render_template('listagem_marketplaces.html', nome=titulo_app, lista=lista)

# @app.route('/listagem_categorias')
# def listagem_categorias():
#     texto = exibir_categorias()
#     return render_template('listagem_categorias.html', nome=titulo_app, listagem=texto)

@app.route('/listagem_categorias')
def listagem_categorias():
    lista = ler_categorias()
    return render_template('listagem_categorias.html', nome=titulo_app, lista=lista)

@app.route('/listagem_subcategorias')
def listagem_subcategorias():
    texto = exibir_subcategorias()
    return render_template('listagem_subcategorias.html', nome=titulo_app, listagem=texto)

app.run(debug=True)