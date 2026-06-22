from flask_appbuilder import BaseView, expose, has_access
from app import db
from app.models.pedido import Pedido
from datetime import datetime, timedelta


class GraficaVentasMesView(BaseView):
    route_base = "/grafica_ventas_mes"
    
    @expose("/")
    @has_access
    def list(self):
        # Últimos 6 meses
        hoy = datetime.now().date()
        meses = []
        montos = []
        
        for i in range(5, -1, -1):
            mes_inicio = hoy.replace(day=1) - timedelta(days=30*i)
            mes_fin = (mes_inicio.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
            
            total = db.session.query(db.func.sum(Pedido.total)).filter(
                Pedido.fecha >= mes_inicio,
                Pedido.fecha <= mes_fin
            ).scalar() or 0
            
            meses.append(mes_inicio.strftime('%b %Y'))
            montos.append(float(total))
        
        return self.render_template(
            "grafica_ventas_mes.html",
            meses=meses,
            montos=montos
        )