from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from app.models.plato import Plato


class PlatoView(ModelView):
    datamodel = SQLAInterface(Plato)
    
    list_columns = ['id', 'nombre', 'precio', 'disponible', 'categoria']
    search_columns = ['nombre', 'categoria']
    add_columns = ['nombre', 'descripcion', 'precio', 'disponible', 'tiempo_preparacion', 'categoria', 'imagen_url']
    edit_columns = ['nombre', 'descripcion', 'precio', 'disponible', 'tiempo_preparacion', 'categoria', 'imagen_url']
    show_columns = ['id', 'nombre', 'descripcion', 'precio', 'disponible', 'tiempo_preparacion', 'categoria', 'imagen_url']
    
    label_columns = {
        'id': 'ID',
        'nombre': 'Nombre',
        'descripcion': 'Descripción',
        'precio': 'Precio',
        'disponible': 'Disponible',
        'tiempo_preparacion': 'Tiempo de Preparación (min)',
        'categoria': 'Categoría',
        'imagen_url': 'URL de la imagen del plato',
    }