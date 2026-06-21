from flask_appbuilder import BaseView, expose
from app import db
from app.models.plato import Plato
from app.models.detalle_pedido import DetallePedido


class ReportePlatosPopularesView(BaseView):
    route_base = "/reporte_platos_populares"
    
    @expose("/")
    def list(self):
        datos = (
            db.session.query(
                Plato.nombre,
                db.func.sum(DetallePedido.cantidad).label('total_vendidos')
            )
            .join(DetallePedido, DetallePedido.plato_id == Plato.id)
            .group_by(Plato.nombre)
            .order_by(db.desc('total_vendidos'))
            .limit(10)
            .all()
        )
        
        return self.render_template(
            "reporte_platos_populares.html",
            platos=[d[0] for d in datos],
            cantidades=[d[1] for d in datos]
        )