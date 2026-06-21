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
        
        # Importar modelos
        from app.models import Cliente, Mesa, Empleado, Categoria, Ingrediente, Plato, PlatoIngrediente, Pedido, DetallePedido
        
        # Importar vistas
        from app.views.categoria_view import CategoriaView
        from app.views.ingrediente_view import IngredienteView
        from app.views.plato_view import PlatoView
        from app.views.cliente_view import ClienteView
        from app.views.mesa_view import MesaView
        from app.views.empleado_view import EmpleadoView
        
        # Registrar vistas en el menú
        appbuilder.add_view(CategoriaView, "Categorías", icon="fa-folder-open", category="Administracion")
        appbuilder.add_view(IngredienteView, "Ingredientes", icon="fa-cube", category="Administracion")
        appbuilder.add_view(PlatoView, "Platos", icon="fa-cutlery", category="Administracion")
        appbuilder.add_view(ClienteView, "Clientes", icon="fa-users", category="Administracion")
        appbuilder.add_view(MesaView, "Mesas", icon="fa-table", category="Administracion")
        appbuilder.add_view(EmpleadoView, "Empleados", icon="fa-user-md", category="Administracion")
        
    return app