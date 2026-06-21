from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from app.models.cliente import Cliente


class ClienteView(ModelView):
    datamodel = SQLAInterface(Cliente)
    
    list_columns = ['id', 'nombre', 'apellido', 'email', 'telefono', 'fecha_registro']
    search_columns = ['nombre', 'apellido', 'email']
    add_columns = ['nombre', 'apellido', 'email', 'telefono', 'direccion']
    edit_columns = ['nombre', 'apellido', 'email', 'telefono', 'direccion']
    show_columns = ['id', 'nombre', 'apellido', 'email', 'telefono', 'direccion', 'fecha_registro']
    
    label_columns = {
        'id': 'ID',
        'nombre': 'Nombre',
        'apellido': 'Apellido',
        'email': 'Email',
        'telefono': 'Teléfono',
        'direccion': 'Dirección',
        'fecha_registro': 'Fecha de Registro'
    }