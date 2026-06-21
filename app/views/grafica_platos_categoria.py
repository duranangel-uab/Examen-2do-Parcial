from flask_appbuilder import BaseView, expose
from app import db
from app.models.categoria import Categoria
from app.models.plato import Plato


class GraficaPlatosCategoriaView(BaseView):
    route_base = "/grafica_platos_categoria"
    
    @expose("/")
    def list(self):
        datos = (
            db.session.query(
                Categoria.nombre,
                db.func.count(Plato.id)
            )
            .join(Plato, Plato.categoria_id == Categoria.id)
            .group_by(Categoria.nombre)
            .all()
        )
        
        return self.render_template(
            "grafica_platos_categoria.html",
            categorias=[d[0] for d in datos],
            cantidades=[d[1] for d in datos]
        )