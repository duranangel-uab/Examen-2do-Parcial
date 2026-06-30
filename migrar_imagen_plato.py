"""
Script de migración: aplica los cambios de estructura necesarios para
el Punto de Venta (POS) sin perder los datos ya existentes.

db.create_all() NO modifica tablas que ya existen, solo crea las que
faltan; por eso este script usa ALTER TABLE directamente.

Cambios que aplica:
  - Tabla "plato": agrega la columna "imagen_url".
  - Tabla "pedido": agrega la columna "para_llevar", y permite que
    "mesa_id" quede vacío (NULL) para pedidos para llevar.

Ejecutar UNA VEZ:

    python migrar_imagen_plato.py
"""
from sqlalchemy import inspect, text

from app import create_app, db

app = create_app()

with app.app_context():
    inspector = inspect(db.engine)

    # --- plato.imagen_url ---
    columnas_plato = [c["name"] for c in inspector.get_columns("plato")]
    if "imagen_url" in columnas_plato:
        print("ℹ️  'plato.imagen_url' ya existe. Nada que hacer.")
    else:
        db.session.execute(text("ALTER TABLE plato ADD COLUMN imagen_url VARCHAR(300)"))
        db.session.commit()
        print("✅ Columna 'imagen_url' agregada a la tabla 'plato'.")

    # --- pedido.para_llevar ---
    columnas_pedido = [c["name"] for c in inspector.get_columns("pedido")]
    if "para_llevar" in columnas_pedido:
        print("ℹ️  'pedido.para_llevar' ya existe. Nada que hacer.")
    else:
        db.session.execute(
            text("ALTER TABLE pedido ADD COLUMN para_llevar BOOLEAN NOT NULL DEFAULT 0")
        )
        db.session.commit()
        print("✅ Columna 'para_llevar' agregada a la tabla 'pedido'.")

    # --- pedido.mesa_id ahora debe permitir NULL (pedidos para llevar) ---
    columnas_info = {c["name"]: c for c in inspector.get_columns("pedido")}
    mesa_id_col = columnas_info.get("mesa_id")
    if mesa_id_col is not None and mesa_id_col.get("nullable") is False:
        try:
            db.session.execute(text("ALTER TABLE pedido MODIFY COLUMN mesa_id INT NULL"))
            db.session.commit()
            print("✅ Columna 'pedido.mesa_id' ahora permite NULL (para pedidos para llevar).")
        except Exception as exc:
            db.session.rollback()
            print(
                "⚠️  No se pudo modificar 'pedido.mesa_id' automáticamente "
                f"({exc}). Si tu base de datos no es MySQL, ejecuta manualmente "
                "el ALTER TABLE correspondiente a tu motor."
            )
    else:
        print("ℹ️  'pedido.mesa_id' ya permite NULL (o no se pudo determinar). Nada que hacer.")

