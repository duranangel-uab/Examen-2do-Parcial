from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.security.decorators import has_access
from flask_appbuilder import expose
from wtforms import SelectField
from app.models.empleado import Empleado
from app.extensions import db


# Lista base de cargos sugeridos. Sirve como punto de partida cuando
# todavía no hay ningún empleado registrado en la base de datos; una vez
# que se registran empleados, sus cargos reales también aparecen como
# opciones (ver _opciones_cargo más abajo).
CARGOS_SUGERIDOS = ["Administrador", "Cajero", "Cocinero", "Mesero"]


def _opciones_cargo():
    """Combina los cargos sugeridos con los cargos que ya existen en la
    base de datos, deduplicados sin distinguir mayúsculas/minúsculas ni
    espacios extra (para que "Mesero" y "mesero " no aparezcan como dos
    opciones distintas en el <select>)."""
    try:
        cargos_existentes = [
            c[0] for c in db.session.query(Empleado.cargo).distinct().all() if c[0]
        ]
    except Exception:
        # La tabla todavía no existe o no hay conexión disponible en
        # este momento; usamos solo los cargos sugeridos como respaldo.
        cargos_existentes = []

    vistos = {}  # clave normalizada (minúsculas, sin espacios extra) -> texto a mostrar
    for cargo in CARGOS_SUGERIDOS + cargos_existentes:
        clave = cargo.strip().lower()
        if clave and clave not in vistos:
            vistos[clave] = cargo.strip()

    return [(texto, texto) for texto in vistos.values()]


class EmpleadoView(ModelView):
    datamodel = SQLAInterface(Empleado)

    add_template = "empleado/add_empleado.html"
    edit_template = "empleado/edit_empleado.html"

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

    # El campo "cargo" se muestra como un select con los cargos ya
    # existentes (más algunos sugeridos), pero permite escribir y
    # guardar un cargo nuevo que no esté en la lista. Flask-AppBuilder
    # solo construye self.add_form/self.edit_form UNA VEZ (al arrancar
    # la app) y los reutiliza siempre después; por eso, para que las
    # opciones del select se mantengan al día con los cargos reales de
    # la base de datos, reconstruimos esos formularios manualmente en
    # cada petición a add()/edit(), justo antes de delegar en la
    # implementación estándar de Flask-AppBuilder.
    def _refrescar_campo_cargo(self):
        from flask_appbuilder.forms import GeneralModelConverter

        campo_cargo = SelectField(
            "Cargo",
            choices=_opciones_cargo(),
            validate_choice=False,
            id="cargo",
        )
        conv = GeneralModelConverter(self.datamodel)
        self.add_form = conv.create_form(
            self.label_columns,
            self.add_columns,
            self.description_columns,
            self.validators_columns,
            {"cargo": campo_cargo},
            self.add_form_query_rel_fields,
        )
        self.edit_form = conv.create_form(
            self.label_columns,
            self.edit_columns,
            self.description_columns,
            self.validators_columns,
            {"cargo": campo_cargo},
            self.edit_form_query_rel_fields,
        )

    @expose("/add", methods=["GET", "POST"])
    @has_access
    def add(self):
        self._refrescar_campo_cargo()
        return super(EmpleadoView, self).add()

    @expose("/edit/<pk>", methods=["GET", "POST"])
    @has_access
    def edit(self, pk):
        self._refrescar_campo_cargo()
        return super(EmpleadoView, self).edit(pk)