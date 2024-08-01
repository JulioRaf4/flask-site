from flask import Flask, render_template
from models import db, Produto
from utils import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///produtos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name)

@app.route('/products/')
@app.route('/products/<name>')
def products(name=None):
    create_and_populate_db()
    produtos = Produto.query.all()
    context = {
        'products': produtos
    }
    return render_template('products.html', name=name, **context)

@app.route('/db')
def show_db():
    produtos = Produto.query.all()
    produto_list = [str(produto) for produto in produtos]
    return '<br>'.join(produto_list)


if __name__ == "__main__":
    app.run(debug=True)
