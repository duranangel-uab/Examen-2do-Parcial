from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_appbuilder import AppBuilder

db = SQLAlchemy()
appbuilder = AppBuilder()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    
    db.init_app(app)
    
    with app.app_context():
        appbuilder.init_app(app, db.session)
        
        # Importar modelos (los crearemos después)
        from app.models import Cliente, Mesa, Empleado, Categoria, Ingrediente, Plato, PlatoIngrediente, Pedido, DetallePedido
        
        # Importar vistas (las crearemos después)
        # from app.views.cliente_view import ClienteView
        # ... etc.
        
    return app