"""
Script para normalizar el campo "cargo" de los empleados ya existentes
en la base de datos.

Problema que resuelve:
    Como el campo "cargo" era originalmente un cuadro de texto libre,
    pueden existir variantes del mismo cargo escritas de forma distinta
    (por ejemplo "Mesero", "mesero", " Mesero "), que el sistema trataba
    como cargos diferentes.

Qué hace:
    Agrupa los cargos sin distinguir mayúsculas/minúsculas ni espacios
    extra, elige una única forma "canónica" para cada grupo (prefiriendo
    los nombres de CARGOS_SUGERIDOS si alguna variante coincide, o si no,
    la variante más usada), y actualiza todos los empleados para que
    todos usen esa misma forma exacta.

Ejecutar UNA VEZ para limpiar datos existentes:

    python normalizar_cargos.py
"""
from collections import Counter

from app import create_app, db
from app.models.empleado import Empleado
from app.views.empleado_view import CARGOS_SUGERIDOS

app = create_app()

with app.app_context():
    empleados = Empleado.query.all()

    # Agrupar empleados por la clave normalizada de su cargo
    grupos = {}
    for emp in empleados:
        if not emp.cargo:
            continue
        clave = emp.cargo.strip().lower()
        grupos.setdefault(clave, []).append(emp)

    sugeridos_por_clave = {c.strip().lower(): c.strip() for c in CARGOS_SUGERIDOS}

    cambios = 0
    for clave, lista_empleados in grupos.items():
        # Elegir la forma canónica: prioridad a los cargos sugeridos,
        # si no, la variante que más se repite entre los empleados.
        if clave in sugeridos_por_clave:
            forma_canonica = sugeridos_por_clave[clave]
        else:
            conteo = Counter(e.cargo.strip() for e in lista_empleados)
            forma_canonica = conteo.most_common(1)[0][0]

        for emp in lista_empleados:
            if emp.cargo != forma_canonica:
                print(f"  {emp.nombre} {emp.apellido}: '{emp.cargo}' -> '{forma_canonica}'")
                emp.cargo = forma_canonica
                cambios += 1

    if cambios:
        db.session.commit()
        print(f"\n✅ {cambios} registro(s) actualizados.")
    else:
        print("\nℹ️  No se encontraron variantes para normalizar. Todo está en orden.")