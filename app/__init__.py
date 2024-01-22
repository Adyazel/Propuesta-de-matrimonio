from flask import Flask
from config import Config
from app.extensions import db, login_manager  # Importa las instancias de extensions.py
from flask_migrate import Migrate
from dotenv import load_dotenv
from celery import Celery
from celery.schedules import crontab
import os

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    return celery

# Creación de la instancia de Flask
app = Flask(__name__)

# Configuración de las variables de la aplicación
app.config.from_object(Config)


# Inicialización de las extensiones
db.init_app(app)  # Aquí utilizas init_app para inicializar db con la aplicación
migrate = Migrate(app, db)
login_manager.init_app(app)  # Inicializa login_manager con la aplicación

# Define la función user_loader
@login_manager.user_loader
def load_user(user_id):
    from app.models import User  # Importa User aquí para evitar importaciones circulares
    return User.query.get(int(user_id))

celery = make_celery(app)

# Cargando los modelos y las rutas
from app import models, routes