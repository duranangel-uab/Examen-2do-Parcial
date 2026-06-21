from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from app.models.ingrediente import Ingrediente


class IngredienteView(ModelView):
    datamodel = SQLAInterface(Ingrediente)
    
    list_columns = ['id', 'nombre', 'unidad', 'stock', 'precio_unitario', 'stock_minimo']
    search_columns = ['nombre']
    add_columns = ['nombre', 'unidad', 'stock', 'precio_unitario', 'stock_minimo']
    edit_columns = ['nombre', 'unidad', 'stock', 'precio_unitario', 'stock_minimo']
    show_columns = ['id', 'nombre', 'unidad', 'stock', 'precio_unitario', 'stock_minimo']
    
    label_columns = {
        'id': 'ID',
        'nombre': 'Nombre',
        'unidad': 'Unidad',
        'stock': 'Stock',
        'precio_unitario': 'Precio Unitario',
        'stock_minimo': 'Stock Mínimo'
    }