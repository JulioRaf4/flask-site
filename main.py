from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name, )

@app.route('/products/')
@app.route('/products/<name>')
def products(name=None):
    products = {
        'product1': {'name': 'Apple', 'price': 1.00, 'description': 'A juicy red apple.'},
        'product2': {'name': 'Banana', 'price': 0.50, 'description': 'A ripe yellow banana.'},
        'product3': {'name': 'Teste', 'price': 0.20, 'description': 'Teste'},
        
    }
    context = {
        'products': products
    }
    return render_template('products.html', name=name, **context)
