from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from app.models.empleado import Empleado


class EmpleadoView(ModelView):
    datamodel = SQLAInterface(Empleado)
    
    list_columns = ['id', 'nombre', 'apellido', 'cargo', 'email', 'activo']
    search_columns = ['nombre', 'apellido', 'cargo']
    add_columns = ['nombre', 'apellido', 'cargo', 'email', 'telefono', 'activo']
    edit_columns = ['nombre', 'apellido', 'cargo', 'email', 'telefono', 'activo']
    show_columns = ['id', 'nombre', 'apellido', 'cargo', 'email', 'telefono', 'fecha_contratacion', 'activo']
    
    label_columns = {
        'id': 'ID',
        'nombre': 'Nombre',
        'apellido': 'Apellido',
        'cargo': 'Cargo',
        'email': 'Email',
        'telefono': 'Teléfono',
        'fecha_contratacion': 'Fecha de Contratación',
        'activo': 'Activo'
    }