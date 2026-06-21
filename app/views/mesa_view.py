from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from app.models.mesa import Mesa


class MesaView(ModelView):
    datamodel = SQLAInterface(Mesa)
    
    list_columns = ['id', 'numero', 'capacidad', 'estado', 'ubicacion']
    search_columns = ['numero', 'estado']
    add_columns = ['numero', 'capacidad', 'estado', 'ubicacion']
    edit_columns = ['numero', 'capacidad', 'estado', 'ubicacion']
    show_columns = ['id', 'numero', 'capacidad', 'estado', 'ubicacion']
    
    label_columns = {
        'id': 'ID',
        'numero': 'Número de Mesa',
        'capacidad': 'Capacidad',
        'estado': 'Estado',
        'ubicacion': 'Ubicación'
    }