from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate.init_app(app, db)

    # CRÍTICO: Importa los modelos AQUÍ para que Flask-Migrate los detecte
    with app.app_context():
        from app.models.paciente import Paciente
        from app.models.medico import Medico
        from app.models.consulta import Consulta

    from app.routes import main
    app.register_blueprint(main)

    return app