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
        
        # Registrar página pública (sin menú)
        appbuilder.add_view_no_menu(PublicView)
        
        # Establecer PublicView como la vista principal (raíz)
        appbuilder.index_view = PublicView

        # Desactivar la redirección automática al login
        appbuilder.auth_views = None

        # Configurar la vista pública sin autenticación
        appbuilder.add_view_no_menu(PublicView)
        appbuilder.index_view = PublicView

        # Desactivar la protección de autenticación para la vista pública
        appbuilder.app.config['AUTH_ROLE_PUBLIC'] = 'Public'
        
    return app