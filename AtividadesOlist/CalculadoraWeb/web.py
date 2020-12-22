from flask import Flask
from calculadora import *

app = Flask(__name__)

@app.route('/')
def index():
    titulo = '<h1> Calculadora </h1>'
    menu = '''
            <ol> 
                <li><a href="/soma"> Soma </a></li>
                <li><a href="/subtracao"> Subtração </a></li>
                <li><a href="/multiplicacao"> Multiplicação </a></li>
                <li><a href="/divisao"> Divisão </a></li>
            </ol>
            '''
    return f'{titulo} {menu}'

@app.route('/soma')    
def somar():
    numero1 = 4.0
    numero2 = 2.0
    resultado = soma(numero1, numero2)
    titulo = '<h1> Calculadora: Soma </h1>'
    conteudo = f'<h3> A soma de 4 + 2 é: {resultado} </h3>'
    voltar = "<a href='/'> Voltar </a>"

    return f'{titulo} {conteudo} <br/> {voltar}'

@app.route('/subtracao')    
def subtrair():
    numero1 = 4.0
    numero2 = 2.0
    resultado = subtracao(numero1, numero2)
    titulo = '<h1> Calculadora: Subtração </h1>'
    conteudo = f'<h3> A ubtração de 4 - 2 é: {resultado} </h3>'
    voltar = "<a href='/'> Voltar </a>"

    return f'{titulo} {conteudo} <br/> {voltar}'

@app.route('/multiplicacao')    
def multiplicar():
    numero1 = 4.0
    numero2 = 2.0
    resultado = multiplicacao(numero1, numero2)
    titulo = '<h1> Calculadora: Multiplicação </h1>'
    conteudo = f'<h3> A multiplicação de 4 * 2 é: {resultado} </h3>'
    voltar = "<a href='/'> Voltar </a>"

    return f'{titulo} {conteudo} <br/> {voltar}'

@app.route('/divisao')    
def dividir():
    numero1 = 4.0
    numero2 = 2.0
    resultado = divisao(numero1, numero2)
    titulo = '<h1> Calculadora: Divisão </h1>'
    conteudo = f'<h3> A divisão de 4 / 2 é: {resultado} </h3>'
    voltar = "<a href='/'> Voltar </a>"

    return f'{titulo} {conteudo} <br/> {voltar}'

app.run()