from flask import Flask
from listagem import *

app = Flask(__name__)

@app.route('/')
def index():
    titulo = '<h1> Listagem </h1>'
    menu = ''' 
           <ol>
            <li><a href="/listagem_marketplaces"> Listagem de Marketplaces </a></li>
            <li><a href="/listagem_categorias"> Listagem de Categorias por Marketplace </a></li>
            <li><a href="/listagem_subcategorias"> Listagem de Subcategorias por Categoria </a></li>
           </ol> 
            '''
    return f'{titulo} {menu}'

@app.route('/listagem_marketplaces')
def listagem_marketplaces():
    texto = exibir_marketplaces()
    titulo = '<h1> Listagem: Marketplaces'
    conteudo = f'<h3> Listagem de Marketplaces: </br> {texto} </h3>'
    voltar = "<a href='/'> Voltar </a>"

    return f'{titulo} {conteudo} <br/> {voltar}'

@app.route('/listagem_categorias')
def listagem_categorias():
    texto = exibir_categorias()
    titulo = '<h1> Listagem: Categorias'
    conteudo = f'<h3> Listagem de Categorias: </br> {texto} </h3>'
    voltar = "<a href='/'> Voltar </a>"

    return f'{titulo} {conteudo} <br/> {voltar}'

@app.route('/listagem_subcategorias')
def listagem_subcategorias():
    texto = exibir_subcategorias()
    titulo = '<h1> Listagem: Subcategorias'
    conteudo = f'<h3> Listagem de Subcategorias: </br> {texto} </h3>'
    voltar = "<a href='/'> Voltar </a>"

    return f'{titulo} {conteudo} <br/> {voltar}'

app.run()