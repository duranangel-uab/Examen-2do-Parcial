import os
from dotenv import load_dotenv
from flask_appbuilder.security.manager import AUTH_DB

basedir = os.path.abspath(os.path.dirname(__file__))

# Carga las variables del archivo .env (ej. GEMINI_API_KEY) como
# variables de entorno reales, accesibles con os.environ.get(...).
# El archivo .env NUNCA debe subirse a GitHub (está en .gitignore).
load_dotenv(os.path.join(basedir, '.env'))

SECRET_KEY = 'clave_secreta_muy_segura_123456789'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/rest_deseo_examen_2do_parcial'
SQLALCHEMY_TRACK_MODIFICATIONS = False

AUTH_TYPE = AUTH_DB
AUTH_ROLE_ADMIN = 'Admin'
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = 'Usuario'

# Hace que la vista pública (app/views/public.py) sea la página de inicio "/"
# en lugar del índice por defecto de Flask-AppBuilder
FAB_INDEX_VIEW = 'app.views.public.PublicView'



# Cambia el nombre que muestra Flask-AppBuilder en el navbar de las
# vistas administrativas (Categorías, Platos, Mesas, etc.), de "F.A.B."
# por defecto a "El Deseo".
APP_NAME = 'El Deseo'

BABEL_DEFAULT_LOCALE = 'es'