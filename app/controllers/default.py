from flask import render_template
from app import app, db

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/cadastro_doenca', methods=['GET', 'POST'])
def cadastro_doenca():
    return render_template('cadastro_doenca.html')

@app.route('/cadastro_epidemiologico', methods=['GET' , 'POST'])
def cadastro_epidemiologico():
    if request.method == 'POST':
        epidemio = Epidemiologico(request.form['data_coleta'], request.form['doenca_associada'])
        db.session.add(epidemio)
        db.session.commit()
        #return redirect(url_for('index'))
    return render_template('cadastro_epidemiologico.html')

@app.route('/visualizacao_doencas', methods=['GET'])
def visualizacao_doencas():
    return render_template('visualizacao_doencas.html')

@app.route('/visualizacao_epidemiologica', methods=['GET'])
def visualizacao_epidemiologica():
    Epidemio = Epidemiologico.query.all()
    return render_template('visualizacao_epidemiologica.html', Epidemio=Epidemio)