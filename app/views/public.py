from flask import render_template
from flask_appbuilder import BaseView, expose, has_access
from app.models.categoria import Categoria
from app.models.plato import Plato
from app.models.pedido import Pedido
from app.models.mesa import Mesa
from app.models.empleado import Empleado
from app.models.cliente import Cliente
from app.extensions import db
from datetime import datetime


class PublicView(BaseView):
    route_base = "/"
    default_view = "index"

    @expose("/")
    def index(self):
        return render_template("public/index.html")

    @expose("/menu")
    def menu(self):
        categorias = Categoria.query.all()
        platos = Plato.query.filter_by(disponible=True).all()
        return render_template("public/menu.html", categorias=categorias, platos=platos)

    @expose("/contacto")
    def contacto(self):
        return render_template("public/contacto.html")

    @expose("/panel")
    @has_access
    def panel(self):
        from flask_login import current_user

        rol = current_user.roles[0].name if current_user.roles else ""
        hoy = datetime.now().date()

        kpis = []
        accesos = []

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

            kpis = [
                {"titulo": "Ventas de hoy", "valor": f"Bs {ventas_hoy:,.2f}", "icono": "💰", "color": "success"},
                {"titulo": "Pedidos pendientes", "valor": pedidos_pendientes, "icono": "🧾", "color": "warning"},
                {"titulo": "Mesas ocupadas", "valor": mesas_ocupadas, "icono": "🍽️", "color": "danger"},
                {"titulo": "Empleados activos", "valor": total_empleados, "icono": "👥", "color": "info"},
            ]
            accesos = [
                {"titulo": "Punto de Venta", "icono": "🧾", "url": "/pos/", "color": "success"},
                {"titulo": "Categorías", "icono": "📂", "url": "/categoriaview/list/", "color": "primary"},
                {"titulo": "Platos", "icono": "🍽️", "url": "/platoview/list/", "color": "primary"},
                {"titulo": "Ingredientes", "icono": "🥗", "url": "/ingredienteview/list/", "color": "primary"},
                {"titulo": "Clientes", "icono": "👤", "url": "/clienteview/list/", "color": "secondary"},
                {"titulo": "Mesas", "icono": "🪑", "url": "/mesaview/list/", "color": "secondary"},
                {"titulo": "Empleados", "icono": "👥", "url": "/empleadoview/list/", "color": "secondary"},
                {"titulo": "Reporte de Ventas", "icono": "📈", "url": "/reporte_ventas/", "color": "success"},
                {"titulo": "Platos Populares", "icono": "🏆", "url": "/reporte_platos_populares/", "color": "success"},
                {"titulo": "Ingredientes Usados", "icono": "📦", "url": "/reporte_ingredientes_usados/", "color": "success"},
                {"titulo": "Gráfica Ventas/Mes", "icono": "📊", "url": "/grafica_ventas_mes/", "color": "info"},
                {"titulo": "Gráfica Platos/Categoría", "icono": "🥘", "url": "/grafica_platos_categoria/", "color": "info"},
                {"titulo": "Gráfica Top Platos", "icono": "⭐", "url": "/grafica_top_platos/", "color": "info"},
            ]

        elif rol == "Supervisor":
            inicio_mes = hoy.replace(day=1)
            ventas_mes = (
                db.session.query(db.func.coalesce(db.func.sum(Pedido.total), 0))
                .filter(Pedido.fecha >= inicio_mes)
                .scalar()
            )
            total_pedidos = Pedido.query.filter(Pedido.fecha >= inicio_mes).count()
            promedio = (ventas_mes / total_pedidos) if total_pedidos > 0 else 0

            kpis = [
                {"titulo": "Ventas del mes", "valor": f"Bs {ventas_mes:,.2f}", "icono": "📈", "color": "success"},
                {"titulo": "Pedidos del mes", "valor": total_pedidos, "icono": "🧾", "color": "info"},
                {"titulo": "Promedio por pedido", "valor": f"Bs {promedio:,.2f}", "icono": "📊", "color": "primary"},
            ]
            accesos = [
                {"titulo": "Punto de Venta", "icono": "🧾", "url": "/pos/", "color": "success"},
                {"titulo": "Reporte de Ventas", "icono": "📈", "url": "/reporte_ventas/", "color": "success"},
                {"titulo": "Platos Populares", "icono": "🏆", "url": "/reporte_platos_populares/", "color": "success"},
                {"titulo": "Ingredientes Usados", "icono": "📦", "url": "/reporte_ingredientes_usados/", "color": "success"},
                {"titulo": "Gráfica Ventas/Mes", "icono": "📊", "url": "/grafica_ventas_mes/", "color": "info"},
                {"titulo": "Gráfica Platos/Categoría", "icono": "🥘", "url": "/grafica_platos_categoria/", "color": "info"},
                {"titulo": "Gráfica Top Platos", "icono": "⭐", "url": "/grafica_top_platos/", "color": "info"},
            ]

        elif rol == "Usuario":
            mesas_disponibles = Mesa.query.filter_by(estado="disponible").count()
            mesas_ocupadas = Mesa.query.filter_by(estado="ocupada").count()
            total_clientes = Cliente.query.count()

            kpis = [
                {"titulo": "Mesas disponibles", "valor": mesas_disponibles, "icono": "🟢", "color": "success"},
                {"titulo": "Mesas ocupadas", "valor": mesas_ocupadas, "icono": "🔴", "color": "danger"},
                {"titulo": "Clientes registrados", "valor": total_clientes, "icono": "👤", "color": "info"},
            ]
            accesos = [
                {"titulo": "Punto de Venta", "icono": "🧾", "url": "/pos/", "color": "success"},
                {"titulo": "Clientes", "icono": "👤", "url": "/clienteview/list/", "color": "primary"},
                {"titulo": "Mesas", "icono": "🪑", "url": "/mesaview/list/", "color": "primary"},
            ]

        return render_template(
            "public/panel.html",
            rol=rol,
            kpis=kpis,
            accesos=accesos,
        )
