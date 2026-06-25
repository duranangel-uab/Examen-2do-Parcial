from flask import jsonify
from flask_appbuilder import BaseView, expose, has_access
from app import db
from app.models.categoria import Categoria
from app.models.plato import Plato
from app.services.ia_pronosticos import generar_pronosticos


class GraficaPlatosCategoriaView(BaseView):
    route_base = "/grafica_platos_categoria"
    
    @expose("/")
    @has_access
    def list(self):
        datos = (
            db.session.query(
                Categoria.nombre,
                db.func.count(Plato.id)
            )
            .join(Plato, Plato.categoria_id == Categoria.id)
            .group_by(Categoria.nombre)
            .all()
        )
        
        return self.render_template(
            "grafica_platos_categoria.html",
            categorias=[d[0] for d in datos],
            cantidades=[d[1] for d in datos]
        )

    @expose("/pronosticos", methods=["POST"])
    @has_access
    def pronosticos(self):
        datos = (
            db.session.query(Categoria.nombre, db.func.count(Plato.id))
            .join(Plato, Plato.categoria_id == Categoria.id)
            .group_by(Categoria.nombre)
            .all()
        )
        resultado = generar_pronosticos(
            contexto="distribución de platos del menú por categoría",
            datos={
                "categorias": [d[0] for d in datos],
                "cantidades": [d[1] for d in datos],
            },
        )
        return jsonify(resultado)