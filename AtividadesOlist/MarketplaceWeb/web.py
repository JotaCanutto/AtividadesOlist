from flask import Flask, render_template
from listagem import *

app = Flask(__name__)

titulo_app = 'Marketplaces'

@app.route('/')
def index():
    listagem_marketplaces = {'nome': 'listar_marketplaces', 'rota': '/listagem_marketplaces'}
    listagem_categorias = {'nome': 'listar_categorias', 'rota': '/listagem_categorias'}
    listagem_subcategorias = {'nome': 'listar_categorias', 'rota': '/listagem_subcategorias'}
    lista = [listagem_marketplaces, listagem_categorias, listagem_subcategorias]
    return render_template('index.html', nome=titulo_app, lista=lista)

@app.route('/listagem_marketplaces')
def listagem_marketplaces():
    texto = exibir_marketplaces()
    return render_template('listagem_marketplaces.html', nome=titulo_app, listagem=texto)

@app.route('/listagem_categorias')
def listagem_categorias():
    texto = exibir_categorias()
    return render_template('listagem_categorias.html', nome=titulo_app, listagem=texto)

@app.route('/listagem_subcategorias')
def listagem_subcategorias():
    texto = exibir_subcategorias()
    return render_template('listagem_subcategorias.html', nome=titulo_app, listagem=texto)

app.run(debug=True)