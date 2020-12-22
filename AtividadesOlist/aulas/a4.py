from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Calculadora </h1>'

@app.route('/soma')
def soma():
    return '<h2> somando... </h2>'

app.run()