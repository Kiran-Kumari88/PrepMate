from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy (but don’t bind to app yet)
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configurations
    app.config['SECRET_KEY'] = 'your_secret_key_here'  # change to something secure
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prepMate.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize db with app
    db.init_app(app)

    # Import models so they are registered with SQLAlchemy
    from . import models  

    # Create database tables if they don’t exist
    with app.app_context():
        db.create_all()

    return app
