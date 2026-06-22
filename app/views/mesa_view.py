from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.fieldwidgets import Select2Widget
from wtforms import SelectField
from app.models.mesa import Mesa


ESTADOS_MESA = [
    ('disponible', 'Disponible'),
    ('ocupada', 'Ocupada'),
    ('reservada', 'Reservada'),
]


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

    # Reemplaza el campo de texto libre "estado" por un menú desplegable
    # con las únicas 3 opciones válidas, tanto al crear como al editar.
    add_form_extra_fields = {
        'estado': SelectField(
            'Estado',
            choices=ESTADOS_MESA,
            widget=Select2Widget()
        )
    }
    edit_form_extra_fields = add_form_extra_fields

    formatters_columns = {
        'estado': lambda item: {
            'disponible': '🟢 Disponible',
            'ocupada': '🔴 Ocupada',
            'reservada': '🟡 Reservada',
        }.get(item, item)
    }