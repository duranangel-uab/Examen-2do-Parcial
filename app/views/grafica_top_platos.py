from flask_appbuilder import BaseView, expose
from app import db
from app.models.plato import Plato
from app.models.detalle_pedido import DetallePedido


class GraficaTopPlatosView(BaseView):
    route_base = "/grafica_top_platos"
    
    @expose("/")
    def list(self):
        datos = (
            db.session.query(
                Plato.nombre,
                db.func.sum(DetallePedido.cantidad).label('total')
            )
            .join(DetallePedido, DetallePedido.plato_id == Plato.id)
            .group_by(Plato.nombre)
            .order_by(db.desc('total'))
            .limit(5)
            .all()
        )
        
        return self.render_template(
            "grafica_top_platos.html",
            platos=[d[0] for d in datos],
            cantidades=[d[1] for d in datos]
        )