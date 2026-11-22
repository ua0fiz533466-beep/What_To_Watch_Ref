from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import settings
db = SQLAlchemy()
migrate = Migrate()
app = Flask(__name__)
app.config.from_object(settings.Config)
db.init_app(app)
migrate.init_app(app, db)
# Импорты в конце, чтобы избежать циклических зависимостей
from opinions_app import views, error_handlers, cli_commands  # noqa: E402,F401
