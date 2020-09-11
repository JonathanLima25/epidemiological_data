from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "<h1>Epidemiological Data</h1>" \
           "Jonathan de Lima Ferreira <strong>RA: 1460481711040</strong></br>" \
           "Professor: Fabricio Galende Marques de Carvalho</br>"



app.run(debug=True, use_reloader=True)