from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()
URI = os.getenv('URI')
KEY = os.getenv('SECRET_KEY')

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    '''
    app.config.update(CELERY_CONFIG={
    'broker_url': 'redis://localhost:6379',
    'result_backend': 'redis://localhost:6379',
        })
        celery = make_celery(flask_app)
    
    '''
    db.init_app(app)

    migrate.init_app(app, db)

    with app.app_context():
        from .Admin.views import admin_bp
        from .Admin.admin_views import Admin_
        app.register_blueprint(Admin_)
        app.register_blueprint(admin_bp)
    return app
