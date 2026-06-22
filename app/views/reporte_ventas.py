from flask import request
from flask_appbuilder import BaseView, expose, has_access
from app import db
from app.models.pedido import Pedido
from app.models.detalle_pedido import DetallePedido
from datetime import datetime, timedelta


class ReporteVentasView(BaseView):
    route_base = "/reporte_ventas"
    
    @expose("/", methods=["GET", "POST"])
    @has_access
    def list(self):
        # Obtener el período seleccionado (por defecto: hoy)
        periodo = request.form.get('periodo', 'hoy')
        
        hoy = datetime.now().date()
        
        if periodo == 'hoy':
            fecha_inicio = hoy
            fecha_fin = hoy
        elif periodo == 'semana':
            fecha_inicio = hoy - timedelta(days=7)
            fecha_fin = hoy
        elif periodo == 'mes':
            fecha_inicio = hoy - timedelta(days=30)
            fecha_fin = hoy
        else:
            fecha_inicio = hoy
            fecha_fin = hoy
        
        # Consulta de ventas
        pedidos = Pedido.query.filter(
            Pedido.fecha >= fecha_inicio,
            Pedido.fecha <= fecha_fin
        ).all()
        
        total_ventas = sum(p.total for p in pedidos)
        total_pedidos = len(pedidos)
        
        # Datos para gráfica (ventas por día)
        ventas_por_dia = {}
        for pedido in pedidos:
            fecha = pedido.fecha.date()
            ventas_por_dia[fecha] = ventas_por_dia.get(fecha, 0) + pedido.total
        
        fechas = sorted(ventas_por_dia.keys())
        montos = [ventas_por_dia[fecha] for fecha in fechas]
        
        return self.render_template(
            "reporte_ventas.html",
            periodo=periodo,
            total_ventas=total_ventas,
            total_pedidos=total_pedidos,
            fechas=fechas,
            montos=montos
        )