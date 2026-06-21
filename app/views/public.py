from flask import render_template
from flask_appbuilder import BaseView, expose
from app.models.categoria import Categoria
from app.models.plato import Plato
from app.extensions import db


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