from flask import jsonify
from flask_appbuilder import BaseView, expose, has_access
from app import db
from app.models.plato import Plato
from app.models.detalle_pedido import DetallePedido
from app.services.ia_pronosticos import generar_pronosticos


class GraficaTopPlatosView(BaseView):
    route_base = "/grafica_top_platos"
    
    @expose("/")
    @has_access
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

    @expose("/pronosticos", methods=["POST"])
    @has_access
    def pronosticos(self):
        datos = (
            db.session.query(Plato.nombre, db.func.sum(DetallePedido.cantidad).label('total'))
            .join(DetallePedido, DetallePedido.plato_id == Plato.id)
            .group_by(Plato.nombre)
            .order_by(db.desc('total'))
            .limit(5)
            .all()
        )
        resultado = generar_pronosticos(
            contexto="top 5 platos más vendidos del restaurante",
            datos={
                "platos": [d[0] for d in datos],
                # MySQL/SQLAlchemy devuelve SUM() como Decimal, que no es
                # serializable a JSON directamente; lo convertimos a int.
                "cantidades": [int(d[1]) for d in datos],
            },
        )
        return jsonify(resultado)