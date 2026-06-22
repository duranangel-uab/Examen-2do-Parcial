from flask import render_template
from flask_appbuilder import BaseView, expose
from flask_login import current_user
from app.models.categoria import Categoria
from app.models.plato import Plato
from app.models.pedido import Pedido
from app.models.mesa import Mesa
from app.models.empleado import Empleado
from app.models.cliente import Cliente
from app.extensions import db
from datetime import datetime, timedelta


class PublicView(BaseView):
    route_base = "/"
    default_view = "index"

    @expose("/")
    def index(self):
        dashboard = None

        if current_user.is_authenticated and current_user.roles:
            rol = current_user.roles[0].name
            hoy = datetime.now().date()

            if rol == "Admin":
                ventas_hoy = (
                    db.session.query(db.func.coalesce(db.func.sum(Pedido.total), 0))
                    .filter(db.func.date(Pedido.fecha) == hoy)
                    .scalar()
                )
                pedidos_pendientes = Pedido.query.filter(
                    Pedido.estado.in_(["pendiente", "en preparacion"])
                ).count()
                mesas_ocupadas = Mesa.query.filter_by(estado="ocupada").count()
                total_empleados = Empleado.query.filter_by(activo=True).count()

                dashboard = {
                    "rol": "Admin",
                    "tarjetas": [
                        {"titulo": "Ventas de hoy", "valor": f"Bs {ventas_hoy:,.2f}", "icono": "💰", "color": "success"},
                        {"titulo": "Pedidos pendientes", "valor": pedidos_pendientes, "icono": "🧾", "color": "warning"},
                        {"titulo": "Mesas ocupadas", "valor": mesas_ocupadas, "icono": "🍽️", "color": "danger"},
                        {"titulo": "Empleados activos", "valor": total_empleados, "icono": "👥", "color": "info"},
                    ],
                }

            elif rol == "Supervisor":
                inicio_mes = hoy.replace(day=1)
                ventas_mes = (
                    db.session.query(db.func.coalesce(db.func.sum(Pedido.total), 0))
                    .filter(Pedido.fecha >= inicio_mes)
                    .scalar()
                )
                total_pedidos = Pedido.query.filter(Pedido.fecha >= inicio_mes).count()
                promedio = (ventas_mes / total_pedidos) if total_pedidos > 0 else 0

                dashboard = {
                    "rol": "Supervisor",
                    "tarjetas": [
                        {"titulo": "Ventas del mes", "valor": f"Bs {ventas_mes:,.2f}", "icono": "📈", "color": "success"},
                        {"titulo": "Pedidos del mes", "valor": total_pedidos, "icono": "🧾", "color": "info"},
                        {"titulo": "Promedio por pedido", "valor": f"Bs {promedio:,.2f}", "icono": "📊", "color": "primary"},
                    ],
                }

            elif rol == "Usuario":
                mesas_disponibles = Mesa.query.filter_by(estado="disponible").count()
                mesas_ocupadas = Mesa.query.filter_by(estado="ocupada").count()
                total_clientes = Cliente.query.count()

                dashboard = {
                    "rol": "Usuario",
                    "tarjetas": [
                        {"titulo": "Mesas disponibles", "valor": mesas_disponibles, "icono": "🟢", "color": "success"},
                        {"titulo": "Mesas ocupadas", "valor": mesas_ocupadas, "icono": "🔴", "color": "danger"},
                        {"titulo": "Clientes registrados", "valor": total_clientes, "icono": "👤", "color": "info"},
                    ],
                }

        return render_template("public/index.html", dashboard=dashboard)

    @expose("/menu")
    def menu(self):
        categorias = Categoria.query.all()
        platos = Plato.query.filter_by(disponible=True).all()
        return render_template("public/menu.html", categorias=categorias, platos=platos)

    @expose("/contacto")
    def contacto(self):
        return render_template("public/contacto.html")