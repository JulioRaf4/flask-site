from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    descricao = db.Column(db.String(120), unique=False, nullable=False)
    img = db.Column(db.String(200), unique=False, nullable=True)

    def __repr__(self):
        return f'<Produto {self.nome}>'
