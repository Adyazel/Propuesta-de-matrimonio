from app import app, db
from app.models import   # Asegúrate de importar tus modelos aquí

with app.app_context():
    db.create_all()

