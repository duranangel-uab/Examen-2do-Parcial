from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from app.models.categoria import Categoria


class CategoriaView(ModelView):
    datamodel = SQLAInterface(Categoria)
    
    list_columns = ['id', 'nombre', 'descripcion']
    search_columns = ['nombre']
    add_columns = ['nombre', 'descripcion']
    edit_columns = ['nombre', 'descripcion']
    show_columns = ['id', 'nombre', 'descripcion']
    
    label_columns = {
        'id': 'ID',
        'nombre': 'Nombre',
        'descripcion': 'Descripción'
    }