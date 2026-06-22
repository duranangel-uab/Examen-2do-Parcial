from flask_appbuilder import BaseView, expose, has_access
from app import db
from app.models.ingrediente import Ingrediente
from app.models.plato_ingrediente import PlatoIngrediente


class ReporteIngredientesUsadosView(BaseView):
    route_base = "/reporte_ingredientes_usados"
    
    @expose("/")
    @has_access
    def list(self):
        datos = (
            db.session.query(
                Ingrediente.nombre,
                db.func.sum(PlatoIngrediente.cantidad).label('total_usado')
            )
            .join(PlatoIngrediente, PlatoIngrediente.ingrediente_id == Ingrediente.id)
            .group_by(Ingrediente.nombre)
            .order_by(db.desc('total_usado'))
            .limit(10)
            .all()
        )
        
        return self.render_template(
            "reporte_ingredientes_usados.html",
            ingredientes=[d[0] for d in datos],
            cantidades=[d[1] for d in datos]
        )