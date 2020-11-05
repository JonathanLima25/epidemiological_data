from app import db

class Doenca(db.Model):
    __tablename__ = "doenca"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    sintomas = db.Column(db.Text)

    def __init__(self, nome, sintomas):
        self.nome = nome
        self.sintomas = sintomas
    
    def __repr__(self):
        return "<Doenca %r>" % self.nome

class Epidemiologico(db.Model):
    __tablename__ = "epidemiologico"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    data_coleta = db.Column(db.String)
    doenca_associada = db.Column(db.String)

    def __init__(self, data_coleta, doenca_associada):
        self.data_coleta = data_coleta
        self.doenca_associada = doenca_associada
    
    def __repr__(self):
        return "<Epidemiologico %r>" % self.doenca_associada