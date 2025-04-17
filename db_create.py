# This script creates the database tables for the Flask application using SQLAlchemy.
from app import app, db

with app.app_context():
    db.create_all()
    print("Tables created!")

