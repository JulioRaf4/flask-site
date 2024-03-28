from flask import Flask, render_template
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///itens.db'
db.init_app(app)

@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name)

@app.route('/products/')
@app.route('/products/<name>')
def products(name=None):
    context = {
        'products': 'products'
    }
    return render_template('products.html', name=name, **context)

@app.route('/db')
def show_db():
    users = User.query.all()
    user_list = [str(user) for user in users]
    return '<br>'.join(user_list)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
