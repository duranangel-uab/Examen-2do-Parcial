import os
from flask_appbuilder.security.manager import AUTH_DB

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'clave_secreta_muy_segura_123456789'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/restaurante_el_deseo'
SQLALCHEMY_TRACK_MODIFICATIONS = False

AUTH_TYPE = AUTH_DB
AUTH_ROLE_ADMIN = 'Admin'
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = 'Usuario'

# Hace que la vista pública (app/views/public.py) sea la página de inicio "/"
# en lugar del índice por defecto de Flask-AppBuilder
FAB_INDEX_VIEW = 'app.views.public.PublicView'

BABEL_DEFAULT_LOCALE = 'es'