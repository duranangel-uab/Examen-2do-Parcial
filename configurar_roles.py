"""
Script para configurar los permisos de los roles Supervisor y Usuario.

Reglas de negocio:
- Admin: acceso total (ya lo asigna Flask-AppBuilder automáticamente
  porque está definido como AUTH_ROLE_ADMIN en config.py).
- Supervisor: puede ver Reportes y Gráficas (análisis del negocio),
  pero NO puede crear/editar/eliminar el catálogo (Categorías, Platos,
  Ingredientes, etc.).
- Usuario: gestión operativa básica del día a día (Pedidos vía Clientes
  y Mesas). No accede a Reportes, Gráficas, ni a la configuración del
  catálogo.

Ejecutar UNA VEZ después de levantar la app por primera vez (o cada vez
que se agreguen vistas nuevas y se quiera re-sincronizar permisos):

    python configurar_roles.py
"""
from app import create_app, db

app = create_app()

# Vistas de solo lectura para Supervisor (reportes y gráficas)
VISTAS_SUPERVISOR = [
    "ReporteVentasView",
    "ReportePlatosPopularesView",
    "ReporteIngredientesUsadosView",
    "GraficaVentasMesView",
    "GraficaPlatosCategoriaView",
    "GraficaTopPlatosView",
]

# Vistas operativas para Usuario (gestión básica del día a día)
VISTAS_USUARIO = [
    "ClienteView",
    "MesaView",
]

# Permisos que se otorgan sobre esas vistas
PERMISOS_LECTURA = ["can_list", "can_show"]
PERMISOS_OPERATIVOS = ["can_list", "can_show", "can_add", "can_edit"]

# Permiso de menú, necesario para que el rol vea el enlace en la barra lateral
PERMISO_MENU = "menu_access"


def asignar_permisos(sm, role, nombres_vistas, nombres_permisos):
    """Asigna a `role` los permisos `nombres_permisos` sobre cada vista
    en `nombres_vistas`, además del acceso de menú correspondiente."""
    for nombre_vista in nombres_vistas:
        # Permisos de acción (can_list, can_show, etc.)
        for nombre_permiso in nombres_permisos:
            pvm = sm.find_permission_view_menu(nombre_permiso, nombre_vista)
            if pvm and pvm not in role.permissions:
                role.permissions.append(pvm)
                print(f"  + {role.name}: {nombre_permiso} en {nombre_vista}")

        # Permiso de menú (para que aparezca el enlace en el panel)
        pvm_menu = sm.find_permission_view_menu(PERMISO_MENU, nombre_vista)
        if pvm_menu and pvm_menu not in role.permissions:
            role.permissions.append(pvm_menu)
            print(f"  + {role.name}: {PERMISO_MENU} en {nombre_vista}")


with app.app_context():
    from app.extensions import appbuilder

    sm = appbuilder.sm

    # --- Crear/obtener el rol Supervisor ---
    supervisor = sm.find_role("Supervisor")
    if not supervisor:
        supervisor = sm.add_role("Supervisor")
        print("✅ Rol 'Supervisor' creado.")
    else:
        print("ℹ️  Rol 'Supervisor' ya existía.")

    # --- Obtener el rol Usuario (ya debería existir por AUTH_USER_REGISTRATION_ROLE) ---
    usuario = sm.find_role("Usuario")
    if not usuario:
        usuario = sm.add_role("Usuario")
        print("✅ Rol 'Usuario' creado.")
    else:
        print("ℹ️  Rol 'Usuario' ya existía.")

    print("\nAsignando permisos a Supervisor (Reportes y Gráficas, solo lectura)...")
    asignar_permisos(sm, supervisor, VISTAS_SUPERVISOR, PERMISOS_LECTURA)

    print("\nAsignando permisos a Usuario (Clientes y Mesas, operativo)...")
    asignar_permisos(sm, usuario, VISTAS_USUARIO, PERMISOS_OPERATIVOS)

    print("\nAsignando acceso al panel interno (/panel) a Supervisor y Usuario...")
    for role in (supervisor, usuario):
        pvm_panel = sm.find_permission_view_menu("can_panel", "PublicView")
        if pvm_panel and pvm_panel not in role.permissions:
            role.permissions.append(pvm_panel)
            print(f"  + {role.name}: can_panel en PublicView")

    db.session.commit()
    print("\n🎉 Roles y permisos configurados exitosamente.")