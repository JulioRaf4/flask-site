from models import db, Produto

def create_and_populate_db():
    db.create_all()
    if not Produto.query.first():
        produtos_iniciais = [
            Produto(nome="Cactus", descricao="Delicious Melted Cactus", img="assets/img/products/3.jpg"),
            Produto(nome="Cherry", descricao="Delicious Cherry", img="assets/img/products/2.jpg")
        ]
        db.session.bulk_save_objects(produtos_iniciais)
        db.session.commit()