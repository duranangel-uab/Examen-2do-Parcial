from flask import Flask
from app.extensions import db, appbuilder


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    
    db.init_app(app)
    
    with app.app_context():
        appbuilder.init_app(app, db.session)
        
        # Importar modelos
        from app.models import Cliente, Mesa, Empleado, Categoria, Ingrediente, Plato, PlatoIngrediente, Pedido, DetallePedido
        
        # Importar vistas CRUD
        from app.views.categoria_view import CategoriaView
        from app.views.ingrediente_view import IngredienteView
        from app.views.plato_view import PlatoView
        from app.views.cliente_view import ClienteView
        from app.views.mesa_view import MesaView
        from app.views.empleado_view import EmpleadoView
        
        # Importar reportes
        from app.views.reporte_ventas import ReporteVentasView
        from app.views.reporte_platos_populares import ReportePlatosPopularesView
        from app.views.reporte_ingredientes_usados import ReporteIngredientesUsadosView
        
        # Importar gráficas
        from app.views.grafica_ventas_mes import GraficaVentasMesView
        from app.views.grafica_platos_categoria import GraficaPlatosCategoriaView
        from app.views.grafica_top_platos import GraficaTopPlatosView
        
        # Importar vista pública
        from app.views.public import PublicView

        # Importar Punto de Venta (POS)
        from app.views.pos_view import PosView

        # Registrar vistas CRUD
        appbuilder.add_view(CategoriaView, "Categorías", icon="fa-folder-open", category="Administracion")
        appbuilder.add_view(IngredienteView, "Ingredientes", icon="fa-cube", category="Administracion")
        appbuilder.add_view(PlatoView, "Platos", icon="fa-cutlery", category="Administracion")
        appbuilder.add_view(ClienteView, "Clientes", icon="fa-users", category="Administracion")
        appbuilder.add_view(MesaView, "Mesas", icon="fa-table", category="Administracion")
        appbuilder.add_view(EmpleadoView, "Empleados", icon="fa-user-md", category="Administracion")
        
        # Registrar reportes
        appbuilder.add_view(ReporteVentasView, "Ventas por período", icon="fa-bar-chart", category="Reportes")
        appbuilder.add_view(ReportePlatosPopularesView, "Platos más vendidos", icon="fa-trophy", category="Reportes")
        appbuilder.add_view(ReporteIngredientesUsadosView, "Ingredientes más usados", icon="fa-cube", category="Reportes")
        
        # Registrar gráficas
        appbuilder.add_view(GraficaVentasMesView, "Ventas por mes", icon="fa-line-chart", category="Gráficas")
        appbuilder.add_view(GraficaPlatosCategoriaView, "Platos por categoría", icon="fa-pie-chart", category="Gráficas")
        appbuilder.add_view(GraficaTopPlatosView, "Top 5 platos", icon="fa-bar-chart", category="Gráficas")

        # Registrar Punto de Venta (sin menú; se accede desde /panel)
        appbuilder.add_view_no_menu(PosView)
        
        # Registrar página pública (sin menú, ya que FAB_INDEX_VIEW en config.py
        # la convierte en la vista raíz "/")
        appbuilder.add_view_no_menu(PublicView)

        # --- Ajuste del botón "Atrás" en los listados/formularios ---
        # Flask-AppBuilder usa appbuilder.get_url_for_index como destino de
        # respaldo del botón "Atrás" cuando no hay suficiente historial de
        # navegación guardado en la sesión. Por defecto eso apunta a la
        # página pública del restaurante (nuestro FAB_INDEX_VIEW). Para que
        # un usuario que ya inició sesión regrese a SU panel (/panel) en
        # vez de la portada pública, sobreescribimos esa propiedad.
        #
        # IMPORTANTE: solo se usa /panel si el usuario realmente tiene
        # permiso de verlo (can_panel). De lo contrario, redirigir siempre
        # a /panel para cualquier usuario autenticado puede causar un
        # bucle infinito de redirecciones cuando ese usuario no tiene el
        # permiso (login -> /panel -> Acceso denegado -> /login -> ...).
        from flask import url_for
        from flask_login import current_user

        def _get_url_for_index_segun_sesion(self):
            if current_user.is_authenticated and self.sm.has_access(
                "can_panel", "PublicView"
            ):
                return url_for("PublicView.panel")
            if self._indexview is None:
                return ""
            return url_for(
                "%s.%s" % (self._indexview.endpoint, self._indexview.default_view)
            )

        type(appbuilder).get_url_for_index = property(_get_url_for_index_segun_sesion)
        
    return app