import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:claire2007@localhost:5432/late_show_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "super-secret"  # Change in production

config = Config()
